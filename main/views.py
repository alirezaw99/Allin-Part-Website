from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact_us.html')

def about_view(request):
    return render(request, 'about_us.html')

def categories_view(request):
    return render(request, 'categories.html')

def parts_list_view(request, slug):
    cat_name = get_object_or_404(Category, slug=slug)
    context = {'cat_name':cat_name}
    return render(request, 'parts_list.html', context)

def parts_detail_view(request):
    return render(request, 'part_single.html')
