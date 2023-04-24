from django.contrib import admin
from .models import Room, Device

class RoomAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'status']
    list_display_links = ['user']
    list_editable = ['name', 'status']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','room', 'name', 'status', 'pwm']
    list_display_links = ['room']
    list_editable = ['name', 'status', 'pwm']

admin.site.register(Room,RoomAdmin)
admin.site.register(Device,DeviceAdmin)