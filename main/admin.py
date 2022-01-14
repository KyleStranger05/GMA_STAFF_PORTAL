from django.contrib import admin
from .models import SettingsClass , ComplexListClass
# Register your models here.


class SettingsAdmin(admin.ModelAdmin):
    pass
admin.site.register(SettingsClass, SettingsAdmin)

class ComplexListAdmin(admin.ModelAdmin):
    pass
admin.site.register(ComplexListClass, ComplexListAdmin)
