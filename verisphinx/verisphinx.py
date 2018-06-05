# -*- coding: utf-8 -*-
"""
    sphinx.domains.verilog
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    The verilog domain.

    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from sphinx import addnodes
from sphinx.domains import Domain, ObjType
from sphinx.locale import l_, _
from sphinx.directives import ObjectDescription
from sphinx.roles import XRefRole
from sphinx.domains.python import _pseudo_parse_arglist
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import GroupedField


class VeriObject(ObjectDescription):
    """
    Description of a verilog object.
    """
    #: If set to ``True`` this object is callable and a `desc_parameterlist` is
    #: added
    has_arguments = True

    #: what is displayed right before the documentation entry
    display_prefix = None

    def handle_signature(self, sig, signode):
        sig = sig.strip()
        prefix = sig

        if '.' in prefix:
            nameprefix, name = prefix.rsplit('.', 1)
        else:
            nameprefix = None
            name = prefix

        objectname     = self.env.ref_context.get('veri:object')
        if nameprefix:
            if objectname:
                # someone documenting the method of an attribute of the current
                # object? shouldn't happen but who knows...
                nameprefix = objectname + '.' + nameprefix
            fullname = nameprefix + '.' + name
        elif objectname:
            fullname = objectname + '.' + name
        else:
            # just a function or constructor
            objectname = ''
            fullname = name

        signode['object'] = objectname
        signode['fullname'] = fullname

        signode += addnodes.desc_annotation(self.display_prefix,
                                            self.display_prefix)
        if nameprefix:
            signode += addnodes.desc_addname(nameprefix + '.', nameprefix + '.')
        signode += addnodes.desc_name(name, name)

        return fullname, nameprefix

    def add_target_and_index(self, name_obj, sig, signode):
        objectname = self.options.get(
            'object', self.env.ref_context.get('veri:object'))
        fullname = name_obj[0]
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname.replace('$', '_S_'))
            signode['first'] = not self.names
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['veri']['objects']
            if fullname in objects:
                self.state_machine.reporter.warning(
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]),
                    line=self.lineno)
            objects[fullname] = self.env.docname, self.objtype

        indextext = self.get_index_text(objectname, name_obj)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname.replace('$', '_S_'),
                                              ''))

    def get_index_text(self, objectname, name_obj):
        name, obj = name_obj
        if self.objtype == 'module':
            return _('%s() (module)') % name
        elif self.objtype == 'struct':
            return _('%s() (struct)')  % name
        return ''

class VeriModule(VeriObject):
    """
    Description of a verilog module
    """
    #: what is displayed right before the documentation entry
    display_prefix = 'module '

    doc_field_types = [
        GroupedField('params', label=l_('Parameter'), rolename='param',
                     names=('parameter','localparam' ),
                     can_collapse=True),
    ]

    
class VeriStruct(VeriObject):
    """
    Description of a verilog module
    """
    #: what is displayed right before the documentation entry
    display_prefix = 'struct '


class VeriXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        # basically what sphinx.domains.python.PyXRefRole does
        refnode['veri:object'] = env.ref_context.get('veri:object')
        if not has_explicit_title:
            title = title.lstrip('.')
            target = target.lstrip('~')
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot+1:]
        if target[0:1] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class VeriDomain(Domain):
    """Verilog language domain."""
    name = 'veri'
    label = 'verilog'
    # if you add a new object type make sure to edit VeriObject.get_index_string
    object_types = {
        'module':  ObjType(l_('module'),  'module'),
        'struct':  ObjType(l_('struct'),  'struct'),        
    }
    directives = {
        'module': VeriModule,
        'struct': VeriStruct,        
    }
    roles = {
        'module': VeriXRefRole(),
        'struct': VeriXRefRole(),        
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
    }

    def clear_doc(self, docname):
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]

    def merge_domaindata(self, docnames, otherdata):
        # XXX check duplicates
        for fullname, (fn, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.data['objects'][fullname] = (fn, objtype)

    def find_obj(self, env, obj, name, typ, searchorder=0):
        if name[-2:] == '()':
            name = name[:-2]
        objects = self.data['objects']
        newname = None
        if searchorder == 1:
            if obj and obj + '.' + name in objects:
                newname = obj + '.' + name
            else:
                newname = name
        else:
            if name in objects:
                newname = name
            elif obj and obj + '.' + name in objects:
                newname = obj + '.' + name
        return newname, objects.get(newname)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        objectname = node.get('veri:object')
        searchorder = node.hasattr('refspecific') and 1 or 0
        name, obj = self.find_obj(env, objectname, target, typ, searchorder)
        if not obj:
            return None
        return make_refnode(builder, fromdocname, obj[0],
                            name.replace('$', '_S_'), contnode, name)

    def resolve_any_xref(self, env, fromdocname, builder, target, node,
                         contnode):
        objectname = node.get('veri:object')
        name, obj = self.find_obj(env, objectname, target, None, 1)
        if not obj:
            return []
        return [('veri:' + self.role_for_objtype(obj[1]),
                 make_refnode(builder, fromdocname, obj[0],
                              name.replace('$', '_S_'), contnode, name))]

    def get_objects(self):
        for refname, (docname, type) in list(self.data['objects'].items()):
            yield refname, refname, type, docname, \
                refname.replace('$', '_S_'), 1            
