# settings/production.py
from .base import *

DEBUG = FALSE

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

