"""
URL configuration for Allin_Part project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,home_view, name='home'),
    path('contact_us/', contact_view, name='contact'),
    path('about_us/', about_view, name='about'),
    path('categories/<slug:cat_name>', categories_view, name='categories'),
    path('parts_list/',  parts_list_view, name='parts_list'),
    path('part_detail/', parts_detail_view, name='parts_detail'),
]
