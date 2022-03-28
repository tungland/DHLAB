__docformat__ = "restructuredtext"

__doc__ = """
Digital Humanities lab
---------------------------
`dhlab` is a python library for accessing reduced representations of text and pictures at
the National Library of Norway (NLN), *Nasjonalbiblioteket* (*NB*) in Norwegian.

It is developed and maintained by `The Digital Humanities lab group <https://www.nb.no/dh-lab/>`_.
"""
__all__ = [
    "nbtext",
    "graph_networkx_louvain",
    "token_map",
    "nbpictures",
    "nb_external_files",
    "module_update",
    "Corpus",
    "Collocations",
    "Concordance"
]
# legacy code
from dhlab.text import nbtokenizer
from dhlab.legacy import (
    nbtext,
    graph_networkx_louvain,
    token_map,
    nbpictures,
    nb_external_files,
    module_update
)

# code from further down in the code tree
from dhlab.text.corpus import Corpus
from dhlab.text.conc_coll import Collocations, Concordance
