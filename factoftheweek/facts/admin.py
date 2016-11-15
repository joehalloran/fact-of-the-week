from django.contrib import admin

# Register your models here.

from .models import Fact

admin.site.register(Fact)