from django.contrib import admin
from loaderio.models import Validation


class ValidationAdmin(admin.ModelAdmin):
    fields = ['token', 'enabled']

admin.site.register(Validation, ValidationAdmin)
