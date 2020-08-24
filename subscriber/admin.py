from django.contrib import admin
from .models import Subscriber, BlacklistWord, GreylistPhrase

# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass

    
@admin.register(BlacklistWord)
class BlacklistWordAdmin(admin.ModelAdmin):
    pass


@admin.register(GreylistPhrase)
class GreylistPhraseAdmin(admin.ModelAdmin):
    pass