#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Kaleko'
HOMEPAGEURL = 'http://davidkaleko.com'
SITENAME = u'From Neutrinos to Data Science'
SITESUBTITLE = u'A Blog that Needs a Better Title'
SITEURL = ''

PATH = 'content'
THEME = 'pelican-clean-blog'

TIMEZONE = 'America/Chicago'
STATIC_PATHS = [ 'CNAME' ]

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['plugins']
PLUGINS = ['ipynb']

GITHUB_URL = 'http://github.com/kaleko'
TWITTER_URL = 'http://twitter.com/davidkaleko'
FACEBOOK_URL = 'http://facebook.com/davidkaleko'

COLOR_SCHEME_CSS = 'github.css'
#others: tomorrow.css, tomorrow_night.css, monokai.css, github.css, darkly.css

#todo: GOOGLE_ANALYTICS
