from django.contrib import admin
from item.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20


admin.site.register(Item, ItemAdmin)
