from django.contrib import admin
from .models import SettingsClass
# Register your models here.


class SettingsAdmin(admin.ModelAdmin):
    pass
admin.site.register(SettingsClass, SettingsAdmin)
