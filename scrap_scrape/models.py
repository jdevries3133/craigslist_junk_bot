from django.db import models


class ListingGroup(models.Model):
    """
    Idk if this makes sense, but something has to bring all these accounts
    together and create a caching layer to reduce requests to the craigslist
    server. It can check the listings in the caching layer before hitting
    craigslist, and try to direct the subscriber to a listing that has already
    been discovered.
    """
    pass