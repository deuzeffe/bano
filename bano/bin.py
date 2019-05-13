from minicli import cli, run

from .core import process


@cli('source', choices=['OSM', 'CADASTRE'])
def process_commune(insee, source, skip_cache=True):
    """ baratin

    :insee: code INSEE de la process_commune
    :source: OSM|CADASTRE
    baratin à la ligne """
    process(insee, source, skip_cache)
  

def main():
    run()