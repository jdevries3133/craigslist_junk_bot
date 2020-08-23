from django.db import models

# Create your models here.
class Conversation(models.Model):
    """
    Storing the information associated with each bot-seller conversation.
    """
    seller_name = models.CharField(max_length=50)
    seller_email = models.CharField(max_length=100)

class Message(models.Model):
    """
    A single message. Two possible types:
        Seller => Both "stb"
        Bot => Seller "bts"
    """
    seller = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    type_ = models.CharField(max_length=10)
    content = models.TextField()