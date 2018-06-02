from .verisphinx import VeriDomain

def setup(app):
    app.add_domain(VeriDomain)
