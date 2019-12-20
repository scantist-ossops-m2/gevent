# -*- coding: utf-8 -*-
#
# gevent documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  1 09:30:02 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import print_function
import sys
import os

# Use the python versions instead of the cython compiled versions
# for better documentation extraction and ease of tweaking docs.
os.environ['PURE_PYTHON'] = '1'

sys.path.append(os.path.dirname(__file__))  # for mysphinxext

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# 1.8 was the last version that runs on Python 2; 2.0+ requires Python 3.
# `autodoc_default_options` was new in 1.8
needs_sphinx = "1.8"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.viewcode',

    # Third-party
    'repoze.sphinx.autointerface',
    'sphinxcontrib.programoutput',

    # Ours
    'mysphinxext',
]

intersphinx_mapping = {
    'http://docs.python.org/': None,
    'https://greenlet.readthedocs.io/en/latest/': None,
    'https://zopeevent.readthedocs.io/en/latest/': None,
    'https://zopecomponent.readthedocs.io/en/latest/': None,
}

extlinks = {'issue': ('https://github.com/gevent/gevent/issues/%s',
                      'issue #'),
            'pr': ('https://github.com/gevent/gevent/pull/%s',
                   'pull request #')}

# Sphinx 1.8+ prefers this to `autodoc_default_flags`. It's documented that
# either True or None mean the same thing as just setting the flag, but
# only None works in 1.8 (True works in 2.0)
autodoc_default_options = {
    'members': None,
    'show-inheritance': None,
}
autodoc_member_order = 'groupwise'
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'gevent'
copyright = u'2009-2019, gevent contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from gevent import __version__
version = __version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = 'obj'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'perldoc'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['gevent.']


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'mytheme'
html_theme_path = ['.']
html_theme_options = {'gevent_version': __version__}
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#if html_theme == 'default':
#    html_theme_options = {'rightsidebar' : True}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Documentation'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# This is true by default in sphinx 1.6
html_use_smartypants = True
smartquotes = True # 1.7

# Custom sidebar templates, maps document names to template names.
html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {'contentstable': 'contentstable.html'}

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'geventdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'gevent.tex', u'gevent Documentation',
     u'gevent contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


###############################################################################


# prevent some stuff from showing up in docs
import socket
import gevent.socket
for item in gevent.socket.__all__[:]:
    if getattr(gevent.socket, item) is getattr(socket, item, None):
        gevent.socket.__all__.remove(item)

if not hasattr(gevent.socket, '_fileobject'):
    # Python 3 building Python 2 docs.
    gevent.socket._fileobject = object()