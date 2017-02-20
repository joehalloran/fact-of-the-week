from django.contrib import admin

from .models import MailContact

class MailContactAdmin(admin.ModelAdmin):
    fields = ('first_name', 'second_name', 'email', 'terms_accepted', 'approved')

admin.site.register(MailContact,  MailContactAdmin)