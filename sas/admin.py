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


@admin.register(sas_models.BusinessPartner)
class BusinessPartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'website_link', 'image_tag']

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No Image'
    
    image_tag.short_description = 'Image'


@admin.register(sas_models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'description', 'project_link', 'image_tag']

    def image_tag(self, obj):
        if obj.project_image:
            return mark_safe(f'<img src="{obj.project_image.url}" width="50" height="50" />')
        return 'No Image'
    
    image_tag.short_description = 'Project Image'

@admin.register(sas_models.SasGallery)
class SasGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'picture', 'image_tag']
    
    def image_tag(self, obj):
        if obj.picture:
            return mark_safe(f'<img src="{obj.picture.url}" width="50" height="50" />')
        return 'No Image'
    
    image_tag.short_description = 'Gallery Image'
    
