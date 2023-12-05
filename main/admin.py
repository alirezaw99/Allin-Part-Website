from django.contrib import admin
from .models import *

# Register your models here.
'''
admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_fa', 'name_en']
    prepopulated_fields  = {'slug':['name_en']}    
    
admin.site.register(Tag)

@admin.register(Model)
class Admin(admin.ModelAdmin):
    list_display = ['model_category', 'model_brand', 'model_name' ]
    list_filter = ['model_brand', 'model_category']
    search_fields = ['model_name']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_number', 'is_onsale']
    list_filter = ['used_models', 'is_onsale', 'in_stock']
    search_fields = ['name', 'part_number']
    
     def formfield_for_manytomany(self, db_field, request, **kwargs):
         if db_field.name == "model_category":
             kwargs["queryset"] = Model.objects.filter(model_category=r)
         return super().formfield_for_manytomany(db_field, request, **kwargs)
'''