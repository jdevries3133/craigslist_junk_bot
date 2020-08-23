from django.db import models

class ScrapListing(models.Model):
    """
    Listings will be stored if they are deemed valid (matching the type that
    the user is looking for), and communication has been initiated with the
    lister.

    Location will be GPS coordinates or 'unknown'. GPS coordinates can be plugged
    into google maps or whatever. They will ultimately come from when the lister
    confirms their location via the conversation.
    """
    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.CharField(max_length=50)  
    scrap_type = models.CharField(max_length=30)
    conversation = models.OneToOneField("communicator.Coversation", on_delete=models.CASCADE)

class CronScrape(models.Model):
    successful = models.BooleanField()
    timestamp = models.DateTimeField(auto_now=True)
    stdout = models.TextField()