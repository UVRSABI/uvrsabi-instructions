# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'UVRSABI'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinxcontrib.youtube",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

youtube_cmd = (
    r"\newcommand{\sphinxcontribyoutube}[3]"
    r"{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    "\n"
)
vimeo_cmd = (
    r"\newcommand{\sphinxcontribvimeo}[3]"
    r"{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    "\n"
)

latex_elements = {"preamble": youtube_cmd + vimeo_cmd}