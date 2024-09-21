from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class BusinessPartner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='companies/images/', blank=True, null=True)
    description = models.TextField()
    website_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name