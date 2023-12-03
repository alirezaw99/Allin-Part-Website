from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Tag)

@admin.register(Auto_Washing_Machine_Model)
class AutoMachineModelAdmin(admin.ModelAdmin):
    search_fields = ['model_name']

@admin.register(Auto_Washing_Machine_Part)
class AutoMachinePartAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_number', 'is_onsale']
    list_filter = ['used_models', 'is_onsale', 'in_stock']
    search_fields = ['name', 'part_number']