from django.contrib import admin

# Register your models here.

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtors')
  list_display_links = ('id', 'title')
  list_filter = ('realtors',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 15

admin.site.register(Listing, ListingAdmin)
