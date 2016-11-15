from django.contrib import admin

# Register your models here.

from .models import MailContact

admin.site.register(MailContact)