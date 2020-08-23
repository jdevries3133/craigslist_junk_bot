from django.contrib import admin
from .models import ScrapListing

# Register your models here.
class ScrapListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScrapListing, ScrapListingAdmin)