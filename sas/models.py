from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class BusinessPartner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='companies/images/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    website_link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class Projects(models.Model):
    project_name = models.CharField(max_length=250, null=True, blank=True)
    project_image = models.FileField(upload_to='projects/images', null=True, blank=True)
    project_link = models.URLField(max_length=250, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class SasGallery(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    picture = models.FileField(upload_to='gallery/images', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class WebPrimaryColor(models.Model):
    color_code = models.CharField(max_length=150, null=True, blank=True)


#About Us Model
class AboutUs(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='about/images', null=True, blank=True)


class SasInfo(models.Model):
    # description = RichTextField(blank=True, null=True)
    address = RichTextField(blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    tiktok = models.URLField(max_length=200, blank=True, null=True)
    pinterest = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.address
    

class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250, blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.designation if self.designation else 'Anonymous'}"
    

class OurClient(models.Model):
    image = models.FileField(upload_to='our_clients/', null=True, blank=True)


# Our Team Model
class OurTeam(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    picture = models.FileField(upload_to='team/', null=True, blank=True)
    facebook = models.URLField(max_length=250, null=True, blank=True)
    linkedin = models.URLField(max_length=250, null=True, blank=True)
    twitter = models.URLField(max_length=250, null=True, blank=True)
    github = models.URLField(max_length=250, null=True, blank=True)


class OurITSection(models.Model):
    criticism = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='criticism/', null=True, blank=True)
