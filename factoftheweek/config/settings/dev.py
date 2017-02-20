# settings/dev.py

from .base import *

DEBUG = True

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ADMINS = [('Joe', 'joe_halloran@hotmail.co.uk')]

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/emails/')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'factoftheweek',
        'USER': 'fotwdbadmin',
        'PASSWORD': 'factoftheweek2016',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'facts': {
        	'handlers': ['console'],
        	'level': 'INFO',
        },
        'mailinglist': {
        	'handlers': ['console'],
        	'level': 'INFO',
        },
    },
}