from __future__ import absolute_import, unicode_literals
import raven

from .base import *

DEBUG = False

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = '.spirestanford.org'

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


STRIPE_API_KEY = "pk_live_FkWgwWDebH6UglEDLHLM2zUi"
STRIPE_SECRET_KEY = "sk_live_KGL53AYVeEzrNhnTgSK4nar9"


GOOGLE_MAPS_V3_APIKEY = "AIzaSyAuAQVs-4VRFdR1-9s94H_CxmMr2QLiYpM"
GEO_WIDGET_DEFAULT_LOCATION = { 'lat': '37.4554996','lng': '-122.1996202,11.96' }


RAVEN_CONFIG = {
    'dsn': 'https://6255be8f3ff84af6a4c1d10f01d1f025:d51cbb84a7a04ed4ac0fde96e8c829a7@sentry.io/193628',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}