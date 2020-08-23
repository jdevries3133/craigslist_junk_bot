from django.db import models
from django.contrib.auth.models import User

class Subscriber(User):
    """
    A subscriber who has configured their subscription. This is a person who
    will pick up scrap.
    """
    pass

class BlacklistWord(models.Model):
    word = models.CharField(max_length=30)
    subscriber = models.OneToOneField("subscriber.Subscriber", on_delete=models.CASCADE)

class GreylistPhrase(models.Model):
    phrase = models.CharField(max_length=100)
    subscriber = models.OneToOneField("subscriber.Subscriber", on_delete=models.CASCADE)
    qset_threshold = models.IntegerField()