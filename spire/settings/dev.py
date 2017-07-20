from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True


SOCIAL_AUTH_FACEBOOK_KEY = '705930582941910'
SOCIAL_AUTH_FACEBOOK_SECRET = '594ee0dbd5353a8984639fa8bb05503c'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.9'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email'
}


DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000


SOCIAL_AUTH_LINKEDIN_KEY = '81dxu2x8vfn5ql'
SOCIAL_AUTH_LINKEDIN_SECRET = 'TVQukKkIMprtrsot'

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address')]


STRIPE_API_KEY = "pk_test_flWrZUy1TeB0z9msSMz67lPY"
STRIPE_SECRET_KEY = "sk_test_es7mrA52AFoENwUyFzOP8SAI"


GOOGLE_MAPS_V3_APIKEY = "AIzaSyCCT4uyy-Z3jbQZ7S6vd7LXz-TSMOtl0M8"
GEO_WIDGET_DEFAULT_LOCATION = { 'lat': '37.4554996','lng': '-122.1996202,11.96' }
