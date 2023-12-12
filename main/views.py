from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.

def home_view(request):
    category = Category.objects.all()
    context = {'category':category}
    
    return render(request, 'home.html', context)

def contact_view(request):
    return render(request, 'contact_us.html')

def about_view(request):
    return render(request, 'about_us.html')

def categories_view(request):
    return render(request, 'categories.html')

def parts_list_view(request, slug):
    try:
        cat_name = Category.objects.get(slug=slug)
        parts = Part.objects.filter(category=cat_name)
        sub_cat = Sub_Category.objects.filter(category=cat_name)
        brands = Model.objects.filter(category=cat_name)
    except (Category.DoesNotExist, UnboundLocalError ) :
        cat_name = get_object_or_404(Sub_Category, slug=slug)
        parts = Part.objects.filter(sub_category=cat_name)
        cat_id = slug.split('-')[-1]
        sub_cat = Sub_Category.objects.filter(category=Category.objects.get(pk=cat_id))
        brands = Model.objects.filter(category=Category.objects.get(pk=cat_id))
    
    context = {'cat_name':cat_name, 'parts':parts, 'sub_cats':sub_cat, 'brands':brands}
    
    return render(request, 'parts_list.html', context)

def parts_detail_view(request):
    return render(request, 'part_single.html')
