from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home_view, name='blog_home'),
    path('<int:id>/', blog_single_view, name='blog_single'),
    path('tag/<slug:slug>/', blog_category_view, name='blog_tag')
]