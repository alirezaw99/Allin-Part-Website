from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish']
    list_filter = ['author', 'publish']
    search_fields = ['title', 'content']
    