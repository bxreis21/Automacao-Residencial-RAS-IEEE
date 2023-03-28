from django.contrib import admin
from .models import Comodo

class ComodoAdmin(admin.ModelAdmin):
    list_display = ['comodo','iluminacao','ventilacao']
    list_display_links = ['comodo']
    

admin.site.register(Comodo, ComodoAdmin)
# Register your models here.
