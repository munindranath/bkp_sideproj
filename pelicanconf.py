#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'mnath'
SITENAME = u'sideproject'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Feeds 
FEEDS =  (('blog', 'feeds/blog.atom.xml'),
          ('project', 'feeds/category/project.atom.xml'),
          ('reading', 'feeds/category/reading.atom.xml'),
          ('Misc', 'feeds/category/misc.atom.xml'),
          )
          

# Social widget

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
          
MENUITEMS = (
             ('home', '/' ),
            )

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = False

# Tell Pelican about directories

STATIC_PATHS = ['images', 'code']

# Specify theme
THEME = "bootstrap"

# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['latex', 'neighbors', 'summary']

# Only use LaTeX for selected articles

LATEX = 'article'
