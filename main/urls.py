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

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,home_view, name='home'),
    path('contact_us/', contact_view, name='contact'),
    path('about_us/', about_view, name='about'),
    path('search/', search_result_view, name='search'),
    path('categories/<slug:slug>',  parts_list_view, name='categories'),
    path('part_detail/<slug:slug>', parts_detail_view, name='part_detail'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login')
]
