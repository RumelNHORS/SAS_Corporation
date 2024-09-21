from django.contrib import admin
from django.utils.html import mark_safe
from sas import models as sas_models

# Register your models here.

# @admin.register(sas_models.Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ['icon', 'title', 'description']


@admin.register(sas_models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon_tag')
    # Method to display the image in the admin list
    def icon_tag(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="50" height="50" />')
        return 'No Image'

    icon_tag.short_description = 'Icon'
