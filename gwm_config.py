# coding: utf-8
################################### WARNING ###################################
#  DON'T CHANGE THIS FILE'S NAME unless you perfectly know what you're doing  #

try:
    from ganeti_webmgr.ganeti_web.settings.local import *
except ImportError:
    from ganeti_webmgr.ganeti_web.settings.base import *


###############################################################################
# List of people to get notification whenever Django encounters errors and
# DEBUG is False
ADMINS = (
    # ('Your name', 'your_email@example.org'),
)

# Who should get notification about broken links (if SEND_BROKEN_LINK_EMAILS is
# set to True)
MANAGERS = ADMINS


###############################################################################
############################### S E C U R I T Y ###############################
# Used for CSRF protection. Use a 16 or 32 bit random string here.
# Do not share this with anyone.
SECRET_KEY = 'CHANGE_ME'
# Ganeti Web Manager helps you with secrets.  You can use one of following
# helpers that load this setting from either environment variable or from
# a file.  In the latter case you can create that file, if it doesn't exist
# yet, with random value.
# SECRET_KEY = load_secret(env='GWM_SECRET_KEY')
# SECRET_KEY = load_secret(env='', file='./.secrets/SECRET_KEY.txt')
# SECRET_KEY = load_secret(env='', file='./.secrets/SECRET_KEY.txt',
#                          create_file=True, overwrite_file=False,
#                          secret_length=50)


###############################################################################
# Database access information.  Uncomment section for the database you're
# using.
# Reminder: Ganeti Web Manager works only with SQLite, MySQL or PostgreSQL!
DATABASES = {
    ### SQLite configuration
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ganeti.db',
        'USER': '',      # not used with SQLite
        'PASSWORD': '',  # not used with SQLite
        'HOST': '',      # not used with SQLite
        'PORT': '',      # not used with SQLite
    },

    ### MySQL configuration
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',  # leave empty for localhost
    #     'PORT': '',  # leave empty for default port
    # },

    ### PostgreSQL configuration
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',  # leave empty for localhost
    #     'PORT': '',  # leave empty for default port
    # }
}


###############################################################################
# Timezones, formatting and localization options
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Los_Angeles'
DATE_FORMAT = "d/m/Y"
DATETIME_FORMAT = "d/m/Y H:i"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en_US'


###############################################################################
# Uncomment below lines if you want to add LDAP-based authentication to Ganeti
# Web Manager:
# AUTHENTICATION_BACKENDS += (
#     'django_auth_ldap.backend.LDAPBackend',
# )


###############################################################################
# Registration settings
ACCOUNT_ACTIVATION_DAYS = 7

# Email settings for registration
EMAIL_HOST = "localhost"
EMAIL_PORT = "25"
# DEFAULT_FROM_EMAIL = "noreply@example.org"

# Whether users should be able to create their own accounts.
# False if accounts can only be created by admins.
ALLOW_OPEN_REGISTRATION = True


##############################################################################
# Ganeti Web Manager specific settings

# Ganeti Cached Cluster Objects Timeouts
#    LAZY_CACHE_REFRESH (milliseconds) is the fallback cache timer that is
#    checked when the object is instantiated. It defaults to 600000ms, or ten
#    minutes.
LAZY_CACHE_REFRESH = 600000

# VNC Proxy. This will use a proxy to create local ports that are forwarded to
# the virtual machines.  It allows you to control access to the VNC servers.
#
# Expected values:
#   String syntax: "HOST:CONTROL_PORT", for example: "localhost:8888". If
#   localhost is used then the proxy will only be accessible to clients and
#   browsers on localhost. Production servers should use a publicly accessible
#   hostname or IP
#
# Firewall Rules:
#   Control Port: 8888, must be open between Ganeti Web Manager and Proxy
#   Internal Ports: 12000+ must be open between the Proxy and Ganeti Nodes
#   External Ports: default is 7000-8000, must be open between Proxy and Client
#   Flash Policy Server: 843, must open between Proxy and Clients
VNC_PROXY = 'localhost:8888'

# PyCurls default TIMEOUT in 7.21.6 defaults to 13 and CONNECTTIMEOUT to 78.
# This is way too long to wait for incorrect or unresponsive ganeti clusters
# when using the rapi for syncing and querying.
RAPI_CONNECT_TIMEOUT = 3

# API Key for authenticating scripts that pull information from ganeti, such as
# list of sshkey's to assign to a virtual machine
#
# XXX this is a temporary feature that will eventually be replaced by a system
#     that automatically creates keys per virtual machine. This is just a quick
#     way of enabled a secure method to pull sshkeys from ganeti web manager
# Remove the # mark to uncomment and replace CHANGE_ME with a secure value.
# WEB_MGR_API_KEY = 'CHANGE_ME'
#
# Just like SECRET_KEY, you can load WEB_MGR_API_KEY contents from either an
# environment variable or a file.  Simply use one of the following helpers:
# WEB_MGR_API_KEY = load_setting_env('GWM_MGR_API_KEY')
# WEB_MGR_API_KEY = load_setting_file('./.secrets/API_KEY.txt')
# WEB_MGR_API_KEY = load_setting_file('./.secrets/API_KEY.txt', create=True)

# Path where to store full-text search indexes.  Relative to this config file.
HAYSTACK_WHOOSH_PATH = here('whoosh_index')
