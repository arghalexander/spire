from __future__ import absolute_import, unicode_literals
import raven

from .base import *

DEBUG = True

#CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = '.spirestanford.org'
CSRF_TRUSTED_ORIGINS =  ['.spirestanford.org',]


SOCIAL_AUTH_FACEBOOK_KEY = '1880382195542856'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c203a4edaf5e3896d55ddeb7eab911cb'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.9'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id,name,email'
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address')]

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '860sj3h07r7oyz'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'w5Werpj0EiyLh0OQ'


STRIPE_API_KEY = "pk_test_flWrZUy1TeB0z9msSMz67lPY"
STRIPE_SECRET_KEY = "sk_test_es7mrA52AFoENwUyFzOP8SAI"


WAGTAILFRONTENDCACHE = {
    'cloudflare': {
        'BACKEND': 'wagtail.contrib.wagtailfrontendcache.backends.CloudflareBackend',
        'EMAIL': 'anthony@spirestanford.org',
        'TOKEN': '2b3f5f2bbd20a1030bc053729d4f02428bece',
        'ZONEID': 'bd7f599c22d18495d9a4d5a3a7be0b3c',
    },
}

GOOGLE_MAPS_V3_APIKEY = "AIzaSyCCT4uyy-Z3jbQZ7S6vd7LXz-TSMOtl0M8"
GEO_WIDGET_DEFAULT_LOCATION = { 'lat': '37.4554996','lng': '-122.1996202,11.96' }


#RAVEN_CONFIG = {
#    'dsn': 'https://6255be8f3ff84af6a4c1d10f01d1f025:d51cbb84a7a04ed4ac0fde96e8c829a7@sentry.io/193628',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
#    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
#}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'spire_staging',
        'USER': 'spire',
        'PASSWORD': 'v6Bh0%MJXuXd%G24',
        'HOST': 'localhost',
        'PORT': '',
    }
}



"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/spire/error.log',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/spire/access.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
"""