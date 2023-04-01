from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'status']
    list_display_links = ['user']
    list_editable = ['name', 'status']

admin.site.register(Room,RoomAdmin)
# Register your models here.
