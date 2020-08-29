from django.contrib import admin
from .models import SubscriberProfile, BlacklistWord, GreylistPhrase

# Register your models here.
@admin.register(SubscriberProfile)
class SubscriberAdmin(admin.ModelAdmin):
    pass

    
@admin.register(BlacklistWord)
class BlacklistWordAdmin(admin.ModelAdmin):
    pass


@admin.register(GreylistPhrase)
class GreylistPhraseAdmin(admin.ModelAdmin):
    pass