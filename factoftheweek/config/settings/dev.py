# settings/dev.py

from .base import *

DEBUG = True

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/emails/')

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