# settings/dev.py
from .base import *

DEBUG = FALSE

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

