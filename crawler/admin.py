from django.contrib import admin
from .models import ScrapListing

# Register your models here.
@admin.register(ScrapListing)
class ScrapListingAdmin(admin.ModelAdmin):
    pass