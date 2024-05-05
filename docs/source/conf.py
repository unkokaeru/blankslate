"""conf.py: configuration file for the Sphinx documentation builder."""

project = "blankslate"
copyright = "2024, William Fayers"
author = "William Fayers"

extensions = ["sphinx.ext.napoleon"]

html_baseurl = "https://blankslate-docs.mydigitalgarden.space/"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_static_path = ["_static"]
