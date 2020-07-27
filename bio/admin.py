from django.contrib import admin
from .models import bio_info,homepage_photos
# Register your models here.

class bio_info_show(admin.ModelAdmin):
    list_display=[
    'name',
    'batch',
    'dept'
    ]
    search_fields=['name']
    list_filter=['batch']
class homepage_photos_show(admin.ModelAdmin):
    list_display=[
    'title',

    ]
    search_fields=['title']
    list_filter=["title"]

admin.site.register(bio_info,bio_info_show)
admin.site.register(homepage_photos,homepage_photos_show)
