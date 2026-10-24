# Configuration file for the Sphinx documentation builder.

project = "InferenceBench documentation (independent sample)"
author = "Mumpe Cydrone"
copyright = "2026, Mumpe Cydrone"

# Markdown support
extensions = ["myst_parser"]
source_suffix = {".md": "markdown"}

# Output theme
html_theme = "furo"
html_title = "InferenceBench docs sample"

exclude_patterns = ["_build"]
