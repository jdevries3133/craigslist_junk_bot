from django.db import models
from django.contrib.auth.models import User

class Subscriber(User):
    """
    A subscriber who has configured their subscription. This is a person who
    will pick up scrap.

    Subscribers can set a custom query to override the default of "scrap metal"
    """
    query = models.CharField(max_length=50, default="scrap metal")


class BlacklistWord(models.Model):
    subscriber = models.OneToOneField("subscriber.Subscriber", on_delete=models.CASCADE)
    word = models.CharField(max_length=30)


class GreylistPhrase(models.Model):
    subscriber = models.OneToOneField("subscriber.Subscriber", on_delete=models.CASCADE)
    phrase = models.CharField(max_length=100)
    qset_threshold = models.IntegerField()