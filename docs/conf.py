#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Scanpy documentation build configuration file, created by
# sphinx-quickstart on Sun Aug 20 00:29:31 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import time
import inspect
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.pardir))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.autosummary',
              #'plot_generator',
              #'plot_directive',
              'numpydoc',
              #'ipython_directive',
              #'ipython_console_highlighting',
              ]


# Generate the API documentation when building
autosummary_generate = True
autodoc_mock_imports = ['_tkinter']
numpydoc_show_class_members = True
numpydoc_class_members_toctree = False

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Scanpy'
copyright = '{}, Alex Wolf, Philipp Angerer'.format(time.strftime("%Y"))
author = 'Alex Wolf, Philipp Angerer'

import scanpy
version = '0.2.6' # scanpy.__version__
release = '0.2.6' # scanpy.__version__
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
# -- Options for HTML output ----------------------------------------------
html_theme = 'sphinx_rtd_theme'
if html_theme == 'sphinx_rtd_theme':
    html_theme_options = {
        'navigation_depth': 2,
    }
    html_context = {
        "display_github": True, # Integrate GitHub
        "github_user": "theislab", # Username
        "github_repo": "scanpy", # Repo name
        "github_version": "master", # Version
        "conf_py_path": "/docs/", # Path in the checkout to the docs root
    }
elif html_theme == 'bootstrap':
    import sphinx_bootstrap_theme
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
    html_theme_options = {
        'navbar_site_name': "Site",
        'navbar_pagenav_name': "Page",
        'source_link_position': "footer",
        'bootswatch_theme': "paper",
        'navbar_pagenav': False,
        'navbar_sidebarrel': False,
        'bootstrap_version': "3",
        'navbar_links': [
            ("API", "api"),
        ],
    }

html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Scanpydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Scanpy.tex', 'Scanpy Documentation',
     'Alex Wolf, Philipp Angerer', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'scanpy', 'Scanpy Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Scanpy', 'Scanpy Documentation',
     author, 'Scanpy', 'One line description of project.',
     'Miscellaneous'),
]


def get_obj_module(qualname):
    """Get a module/class/attribute and its original module by qualname"""
    modname = qualname
    classname = None
    attrname = None
    while modname not in sys.modules:
        attrname = classname
        modname, classname = modname.rsplit('.', 1)

    # retrieve object and find original module name
    if classname:
        cls = getattr(sys.modules[modname], classname)
        modname = cls.__module__
        obj = getattr(cls, attrname) if attrname else cls
    else:
        obj = None

    return obj, sys.modules[modname]


def get_linenos(obj):
    """Get an object’s line numbers"""
    lines, start = inspect.getsourcelines(obj)
    return start, start + len(lines) - 1


project_dir = Path(__file__).parent.parent  # project/docs/conf.py/../.. → project/
github_url = 'https://github.com/{github_user}/{github_repo}/tree/{github_version}'.format_map(html_context)
def modurl(qualname):
    """Get the full GitHub URL for some object’s qualname"""
    obj, module = get_obj_module(qualname)
    path = Path(module.__file__).relative_to(project_dir)
    fragment = '#L{}-L{}'.format(*get_linenos(obj)) if obj else ''
    return '{}/{}{}'.format(github_url, path, fragment)


# html_context doesn’t apply to autosummary templates ☹
# and there’s no way to insert filters into those templates
# so we have to modify the default filters
from jinja2.defaults import DEFAULT_FILTERS

DEFAULT_FILTERS['modurl'] = modurl

