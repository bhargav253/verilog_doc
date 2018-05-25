#!/usr/bin/python2.7

import re,io

veri = open('encoder.v', 'rt')
text = veri.readlines()

for line in text:
    m = re.match(r'\bmodule\s+(\w+)\s*',line)
    if m:
        print "module: " + m.group(1)

    m = re.match(r'/\*',line)
    if m:
        print "block_comment: " + m.group(0)

    m = re.match(r'//#+(.*)\n',line)
    if m:
        print "metacomment: " + m.group(1)
