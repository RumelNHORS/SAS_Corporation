from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class BusinessPartner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='companies/images/', blank=True, null=True)
    description = models.TextField()
    website_link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class Projects(models.Model):
    project_name = models.CharField(max_length=250, null=True, blank=True)
    project_image = models.FileField(upload_to='projects/images', null=True, blank=True)
    project_link = models.URLField(max_length=250, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class SasGallery(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    picture = models.FileField(upload_to='gallery/images', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class WebPrimaryColor(models.Model):
    color_code = models.CharField(max_length=150, null=True, blank=True)