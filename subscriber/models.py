from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SubscriberProfile(models.Model):
    """
    A subscriber who has configured their subscription. This is a person who
    will pick up scrap.

    Subscribers can set a custom query to override the default of "scrap metal"
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=50, default="scrap metal")
    pickup_range = models.IntegerField(_("Pickup Range (miles)"), default=8)
    is_available_for_pickup = models.BooleanField(default=False)


class BlacklistWord(models.Model):
    subscriber = models.ForeignKey(SubscriberProfile, on_delete=models.CASCADE)
    word = models.CharField(max_length=30)


class GreylistPhrase(models.Model):
    subscriber = models.ForeignKey(SubscriberProfile, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=100)
    qset_threshold = models.IntegerField(default=60)