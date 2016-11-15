# settings/dev.py

from .base import *

DEBUG = True

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']