# settings/production.py
from .base import *

DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Static file

STATIC_ROOT = os.path.join(BAS_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BAS_DIR, 'static'),
)
