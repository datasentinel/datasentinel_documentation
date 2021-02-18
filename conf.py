# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Datasentinel - PostgreSQL performance monitoring tool'
copyright = '2020-2021 Datasentinel for Postgres'
author = 'Datasentinel'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'rinoh.frontend.sphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_static_path = ['_static']
html_theme = 'sphinx_materialdesign_theme'
html_title = 'Datasentinel'
html_logo = '_static/datasentinel_logo_with_text.png'
html_favicon = '_static/favicon.png'

html_css_files = [
    'datasentinel.css',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_theme_options = {
    'header_links' : [
        ('Home', 'index', False, 'home'),
        ('Web site', "https://www.datasentinel.io", True, 'link'),
        ('Github', "https://github.com/datasentinel", True, 'link'),
        ('Live demo', "https://demo.datasentinel.io", True, 'dashboard'),
    ],
    'primary_color': 'indigo',
    'fixed_drawer': True,
    'fixed_header': False,
    'header_waterfall': True,
    'header_scroll': False,
    'show_header_title': False,
    'show_drawer_title': True,
    'show_footer': True
}

