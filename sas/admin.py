from django.contrib import admin
from django.utils.html import mark_safe, strip_tags
from django.utils.text import Truncator 
from sas import models as sas_models
from ckeditor.widgets import CKEditorWidget
from django import forms

# Register your models here.

admin.site.register(sas_models.OurClient)

# Service Admin Form
class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = sas_models.Service
        fields = '__all__'

@admin.register(sas_models.Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('title', 'short_description', 'icon_tag')

    def short_description(self, obj):
        plain_text = strip_tags(obj.description)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text

    def icon_tag(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="50" height="50" />')
        return 'No Image'
    
    icon_tag.short_description = 'Icon'

# BusinessPartner Admin Form
class BusinessPartnerAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = sas_models.BusinessPartner
        fields = '__all__'

@admin.register(sas_models.BusinessPartner)
class BusinessPartnerAdmin(admin.ModelAdmin):
    form = BusinessPartnerAdminForm
    list_display = ['name', 'short_description', 'website_link', 'image_tag']
    
    def short_description(self, obj):
        plain_text = strip_tags(obj.description)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No Image'
    
    image_tag.short_description = 'Image'


# Projects Admin Form
class ProjectsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = sas_models.Projects
        fields = '__all__'

@admin.register(sas_models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    form = ProjectsAdminForm
    list_display = ['project_name', 'short_description', 'project_link', 'image_tag']

    def short_description(self, obj):
        plain_text = strip_tags(obj.description)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text

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

admin.site.register(sas_models.WebPrimaryColor)
# admin.site.register(sas_models.SasInfo)


# AboutUs Admin Form
class AboutUsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = sas_models.AboutUs
        fields = '__all__'

@admin.register(sas_models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm
    list_display = ['title', 'short_description', 'image_tag']

    def short_description(self, obj):
        plain_text = strip_tags(obj.description)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No Image'
    
    image_tag.short_description = 'About Image'

class SasInfoAdminForm(forms.ModelForm):
    address = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = sas_models.SasInfo
        fields = '__all__'

class SasInfoAdmin(admin.ModelAdmin):
    form = SasInfoAdminForm
    list_display = ['formatted_address']

    def formatted_address(self, obj):
        plain_text = strip_tags(obj.address)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text

    formatted_address.short_description = 'Address'

    def Address(self, obj):
        plain_text = strip_tags(obj.address)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text

admin.site.register(sas_models.SasInfo, SasInfoAdmin)


class TestimonialAdminForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = sas_models.Testimonial
        fields = '__all__'

@admin.register(sas_models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialAdminForm
    list_display = ['name', 'designation', 'formatted_message', 'image_tag']

    def formatted_message(self, obj):
        plain_text = strip_tags(obj.message)
        truncated_text = Truncator(plain_text).chars(50, truncate='...')
        return truncated_text
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No Image'
    
    image_tag.short_description = 'Testimonial Image'

admin.site.register(sas_models.OurTeam)
