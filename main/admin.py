from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_fa', 'name_en']
    prepopulated_fields  = {'slug':['name_en']}    
    
admin.site.register(Tag)

@admin.register(Model)
class Admin(admin.ModelAdmin):
    search_fields = ['model_name']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_number', 'is_onsale']
    list_filter = ['used_models', 'is_onsale', 'in_stock']
    search_fields = ['name', 'part_number']