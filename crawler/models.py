from django.db import models

# Create your models here.
class ScrapListing(models.Model):
    title = models.CharlField(max_length=30)
    description = models.models.TextField()
    location = models.CharField(max_length=50)  # gps coordinates
