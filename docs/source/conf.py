# Configuration file for the Sphinx documentation builder.

import toml

# -- Project information

project = "django-fbv"
copyright = "2022, Adam Hill"
author = "Adam Hill"

pyproject = toml.load("../../pyproject.toml")
version = pyproject["tool"]["poetry"]["version"]
release = version


# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "furo"

# -- Options for EPUB output
epub_show_urls = "footnote"

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

myst_heading_anchors = 3
myst_enable_extensions = ["linkify", "colon_fence"]
