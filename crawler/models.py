from django.db import models
from django.utils.translation import ugettext_lazy as _

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
    latitude = models.DecimalField(max_digits=7, decimal_places=6)
    longitude = models.DecimalField(max_digits=7, decimal_places=6)
    scrap_type = models.CharField(max_length=30)


class ScrapeReport(models.Model):
    """
    Every hour, do a scrape for every user that is logged in. However, also do
    a scrape when users first checks in.
    """
    successful = models.BooleanField()
    timestamp = models.DateTimeField(auto_now=True)
    stdout = models.TextField()
    scrap_type = models.CharField(_("Scrape Type (Check-in-prompted, or cron)"), max_length=50)