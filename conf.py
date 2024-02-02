# -*- coding: utf-8 -*-
#
# Understanding Accounting For Entrepreneurs documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  3 10:57:29 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
DIR = os.path.dirname(__file__)
sys.path.insert(
    0, os.path.abspath(
        os.path.join(DIR, '_extensions')))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'odoo',
    'demo_link',
    'embedded_video',
    'github_link',
    'html_domain',
    'redirects',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Odoo'
copyright = u'2015-TODAY, Odoo S.A.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '14.0'
version = '14.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    # translations
    'locale',
    'README.*',
    # virtualenv
    'bin', 'include', 'lib',
]

# The specifications of redirect rules used by the redirects extension.
redirects_file = 'redirects.txt'

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'odoo'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'odoo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'nosidebar': 'true',
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_extensions']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

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
html_static_path = ['_static']
html_add_permalinks = ''

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'UnderstandingAccountingForEntrepreneursdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {

# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': r'\usepackage{odoo}',
'tableofcontents': r'', # no TOC

# output manually in latex docs
'releasename': '',
}

latex_additional_files = ['_static/latex/odoo.sty']

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('legal/terms/enterprise_tex', 'odoo_enterprise_agreement.tex', 'Odoo Enterprise Subscription Agreement', '', 'howto'),
  ('legal/terms/partnership_tex', 'odoo_partnership_agreement.tex', 'Odoo Partnership Agreement', '', 'howto'),
  ('legal/terms/terms_of_sale', 'terms_of_sale.tex', 'Odoo Terms of Sale', '', 'howto'),

  ('legal/terms/i18n/enterprise_tex_fr', 'odoo_enterprise_agreement_fr.tex', 'Odoo Enterprise Subscription Agreement (FR)', '', 'howto'),
  ('legal/terms/i18n/partnership_tex_fr', 'odoo_partnership_agreement_fr.tex', 'Odoo Partnership Agreement (FR)', '', 'howto'),
  ('legal/terms/i18n/terms_of_sale_fr', 'terms_of_sale_fr.tex', u'Conditions Générales de Vente Odoo', '', 'howto'),

  ('legal/terms/i18n/enterprise_tex_nl', 'odoo_enterprise_agreement_nl.tex', 'Odoo Enterprise Subscription Agreement (NL)', '', 'howto'),
  #('legal/terms/i18n/partnership_tex_nl', 'odoo_partnership_agreement_nl.tex', 'Odoo Partnership Agreement (NL)', '', 'howto'),

  ('legal/terms/i18n/enterprise_tex_de', 'odoo_enterprise_agreement_de.tex', 'Odoo Enterprise Subscription Agreement (DE)', '', 'howto'),
  #('legal/terms/i18n/partnership_tex_de', 'odoo_partnership_agreement_de.tex', 'Odoo Partnership Agreement (DE)', '', 'howto'),

  ('legal/terms/i18n/enterprise_tex_es', 'odoo_enterprise_agreement_es.tex', 'Odoo Enterprise Subscription Agreement (ES)', '', 'howto'),
  ('legal/terms/i18n/partnership_tex_es', 'odoo_partnership_agreement_es.tex', 'Odoo Partnership Agreement (ES)', '', 'howto'),

  #('index', 'UnderstandingAccountingForEntrepreneurs.tex', u'Understanding Accounting For Entrepreneurs Documentation', u'fp, xmo', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/icons/odoo_logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = "True"

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'understandingaccountingforentrepreneurs', u'Understanding Accounting For Entrepreneurs Documentation',
     [u'fp, xmo'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'UnderstandingAccountingForEntrepreneurs', u'Understanding Accounting For Entrepreneurs Documentation',
   u'fp, xmo', 'UnderstandingAccountingForEntrepreneurs', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

odoo_cover_external = {}

github_user = 'odoo'
github_project = 'documentation-user'

# Where are stored the localisations files
locale_dirs = ['locale/']

LANGUAGES = {
    'de': 'German',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'hr': 'Croatian',
    'nl': 'Dutch',
    'pt_BR': 'Portuguese (BR)',
    'uk': 'Ukrainian',
    'zh_CN': 'Chinese',
}

def setup(app):
    app.add_stylesheet('accounting.css')
    app.add_stylesheet('legal.css')
    app.add_javascript('prefixfree.min.js')
    app.add_javascript('atom.js')
    app.add_javascript('immutable.js')
    app.add_javascript('react.min.js')
    app.add_javascript('accounts.js')
    app.add_javascript('chart-of-accounts.js')
    app.add_javascript('entries.js')
    app.add_javascript('reconciliation.js')
    app.add_javascript('misc.js')

    app.add_javascript('inventory.js')
    app.add_javascript('coa-valuation-continental.js')
    app.add_javascript('coa-valuation-anglo-saxon.js')

    app.connect('html-page-context', canonicalize)
    app.add_config_value('canonical_root', None, 'env')
    app.add_config_value('canonical_branch', 'master', 'env')

    app.connect('html-page-context', analytics)
    app.add_config_value('google_analytics_key', '', 'env')

    app.connect('html-page-context', versionize)
    app.add_config_value('versions', '', 'env')

    app.connect('html-page-context', localize)
    app.add_config_value('languages', '', 'env')

    app.connect('doctree-resolved', tag_toctrees)

def versionize(app, pagename, templatename, context, doctree):
    """ Adds a version switcher below the menu, requires ``canonical_root``
    and ``versions`` (an ordered, space-separated lists of all possible
    versions).
    """
    if not (app.config.canonical_root and app.config.versions):
        return

    # remove last fragment containing the version
    root = '/'.join(app.config.canonical_root.rstrip('/').split('/')[:-1])

    context['versions'] = [
        (vs, _build_url(root, vs, pagename))
        for vs in app.config.versions.split(',')
        if vs != app.config.version
    ]

def analytics(app, pagename, templatename, context, doctree):
    if not app.config.google_analytics_key:
        return

    context['google_analytics_key'] = app.config.google_analytics_key

def tag_toctrees(app, doctree, docname):
    """ Adds a 'toc' metadata entry to all documents containing a toctree node"""
    # document
    #   section
    #     title
    #     compound@toctree-wrapper
    #     ....
    if not len(doctree.children) == 1:
        return
    [section] = doctree.children
    if len(section.children) < 2:
        return
    compound = section.children[1]
    if 'toctree-wrapper' not in compound['classes']:
        return

    app.env.metadata[docname]['has-toc'] = True

def localize(app, pagename, templatename, context, doctree):
    """ Adds a language switcher below the menu, requires ``canonical_root``
    and ``languages`` (an ordered, space-separated lists of all possible
    languages).
    """
    if not (app.config.canonical_root and app.config.languages):
        return

    current_lang = app.config.language or 'en'
    context['language'] = LANGUAGES.get(current_lang, current_lang.upper())
    context['languages'] = [
        (LANGUAGES.get(la, la.upper()), _build_url(app.config.canonical_root, (la != 'en' and la or ''), pagename))
        for la in app.config.languages.split(',')
        if la != current_lang
    ]
    context['language_codes'] = [
        (la.split('_')[0] if la != 'en' else 'x-default', _build_url(app.config.canonical_root, (la != 'en' and la or ''), pagename))
        for la in app.config.languages.split(',')
    ]

def canonicalize(app, pagename, templatename, context, doctree):
    """ Adds a 'canonical' URL for the current document in the rendering
    context. Requires the ``canonical_root`` setting being set. The canonical
    branch is ``master`` but can be overridden using ``canonical_branch``.
    /documentation/user/12.0/sale.html -> /documentation/user/13.0/sale.html
    /documentation/user/11.0/fr/website.html -> /documentation/user/13.0/fr/website.html
    """
    if not app.config.canonical_root:
        return

    # remove last fragment containing the version
    root = '/'.join(app.config.canonical_root.rstrip('/').split('/')[:-1])
    root += '/' + app.config.canonical_branch
    current_lang = app.config.language or 'en'

    context['canonical'] = _build_url(
        root, (current_lang != 'en' and current_lang or ''), pagename)

def _build_url(root, branch, pagename):
    root = root.rstrip('/')
    if branch:
        root += '/'
    return "{canonical_url}{canonical_branch}/{canonical_page}".format(
        canonical_url=root,
        canonical_branch=branch,
        canonical_page=(pagename + '.html').replace('index.html', '')
                                           .replace('index/', ''),
    )
