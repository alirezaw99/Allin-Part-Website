from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Brand, Category, Part

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact_us.html')

def about_view(request):
    return render(request, 'about_us.html')

def categories_view(request):
    return render(request, 'categories.html')

def parts_list_view(request):
    return render(request, 'parts_list.html')

def parts_detail_view(request):
    return render(request, 'part_single.html')
