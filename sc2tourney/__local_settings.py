# Local settings for sc2tourney project.
LOCAL_SETTINGS = True
from settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sc2tourney',
    }
}

INSTALLED_APPS += ['debug_toolbar']

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
