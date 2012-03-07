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
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
