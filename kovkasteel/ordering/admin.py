from django.contrib import admin

from .models import Client
from django.utils.safestring import mark_safe

# Register your models here.

class ClientADmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'email', 'message', 'photo')
    list_display_links = ('name', 'phone')
    search_fields = ('name', 'phone')



admin.site.register(Client, ClientADmin)




# class ClientAdmin(admin.ModelAdmin):
#
#     readonly_fields = ["preview"]
#
#     def preview(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}">')