# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parent.resolve().as_posix())
sys.path.insert(0, pathlib.Path(__file__).parent.joinpath("../dhlab").resolve().as_posix())
print(sys.path)

# -- download notebooks --------------------------

from dhlab.utils.files import download_from_github, working_directory


filenames = [
    'Oppstart.ipynb',
    '1_Bygg_korpus.ipynb',
    '2_Konkordans.ipynb',
    '3_Kollokasjoner.ipynb',
    '4_N-gram_og_galakser.ipynb',
    '5_Navnegrafer.ipynb',
    '6_Søk_med_trunkering.ipynb',
    '7_Setningsuttrekk.ipynb',
    '8_Sammenlign_metadata.ipynb',
    '9_Ordparadigmer.ipynb',
    '10_Søk_i_aviser.ipynb',
    '10_Frekvenslister.ipynb',
    'Anbefalt_lesning.ipynb',
]

with working_directory("./notebooks"):
    for filename in filenames:
        download_from_github(
            filename=filename,
            user="NationalLibraryOfNorway",
            repository='digital_tekstanalyse',
            branch='develop',
            overwrite=False,
            silent=True)


# -- Project information -----------------------------------------------------

project = 'digital_tekstanalyse'
author = 'DH-lab, National Library of Norway'
email = 'dh-lab@nb.no'
copyright = f'2022, {author}'
version = '2.0'
# The full version, including alpha/beta/rc tags
release = 'v2.0.22'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Sphinx's own extensions
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.imgconverter',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.linkcode',
    'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    # 'sphinx.ext.jsmath',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',

    'myst_parser',  # Markdownparser
    'sphinx_inline_tabs',  # Tab switches
    'nbsphinx',  # Integrate jupyter notebooks
    #"'sphinx_gallery.load_style',
    'sphinx_togglebutton',
    'sphinx_copybutton',
]

#
# # Extension written directly in the conf.py file
# def linkcode_resolve(domain, info):
#     if domain != 'py':
#         return None
#     if not info['module']:
#         return None
#     filename = info['module'].replace('.', '/')
#     return "https://github.com/NationalLibraryOfNorway/DHLAB/blob/main/%s.py" % filename
#

autosectionlabel_prefix_document = True

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'  # 'nb_NO'

# The master toctree document.
root_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "py:obj"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

todo_include_todos = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries


autodoc_default_options = {
    'members': True,  # 'var1, var2',
    'member-order': 'groupwise', # or 'alphabetical' or 'bysource'
    #'special-members': '__init__',
    'undoc-members': True,
    'private-members': False,
    'exclude-members': '__weakref__',
    'inherited-members': True,
    'show-inheritance': True,
    #'ignore-module-all': False,
    #'imported-members': False,
    #'class-doc-from': None,
    #'no-value': False,
}


# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
}

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d %B %Y'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
pygments_dark_style = "monokai"

# Jupyter Notebook options ####################

#nbsphinx_custom_formats = {
#    ".md": ["jupytext.reads", {"fmt": "mystnb"}],
#}

togglebutton_hint = "Show"
togglebutton_hint_hide = "Hide"


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'. See the documentation for
# # a list of builtin themes.
html_theme = 'furo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#33C1CC",
        "color-brand-content": "teal",
        # "color-admonition-background": "cyan",
    },
    "dark_css_variables": {
        "color-brand-primary": "#33C1CC",
        "color-brand-content": "teal",
        # "color-admonition-background": "cyan",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,

}

html_css_files = [
    'dhlab/css_style_sheets/grade3.css',
    'dhlab/css_style_sheets/monokai.css',
    'dhlab/css_style_sheets/nb_notebook_2.css',
    'dhlab/css_style_sheets/nb_notebook_blue.css',
    'dhlab/css_style_sheets/nb_notebook.css'
]

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'dhlab'

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_images/dhlab_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_images/nb_symbol_farge_z5B_icon.ico"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}


# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'dhlab_docs'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'dhlab.tex', u'DHLAB Documentation',
     u'Lars Johnsen, '
     u'Magnus Breder Birkenes, '
     u'Andre Kåsen, '
     u'Yngvil Beyer, '
     u'Ingerid Løyning Dale',
     'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


# -- Options for EPUB output --------------------------------------------------

# EPUB options
epub_show_urls = 'footnote'
