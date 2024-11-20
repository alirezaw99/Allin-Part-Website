from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    
    
@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'author', 'publish']
    list_filter = ['author', 'publish']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    