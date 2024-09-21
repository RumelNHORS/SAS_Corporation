from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title