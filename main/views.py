from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import *


# Create your views here.

def home_view(request):
    category = Category.objects.all()
    parts = Part.objects.filter(popular=1)
    
    context = {'category':category, 'parts':parts}
    
    return render(request, 'home.html', context)

def contact_view(request):
    return render(request, 'contact_us.html')

def about_view(request):
    return render(request, 'about_us.html')

def search_result_view(request):
    search_part = request.GET.get('search')
    if search_part : 
        parts = Part.objects.filter(Q(name__contains=search_part))
    else :
        parts = Part.objects.all()
   
    context = {'parts':parts, 'search_part':search_part}
    
    return render(request, 'search_result.html', context)

def parts_list_view(request, slug):
    try:
        cat_name = Category.objects.get(slug=slug)
        main_cat = Category.objects.get(slug=slug)
        parts = Part.objects.filter(category=cat_name)
        sub_cat = Sub_Category.objects.filter(category=cat_name)
    except (Category.DoesNotExist, UnboundLocalError ) :
        cat_id = slug.split('-')[-1]
        cat_name = get_object_or_404(Sub_Category, slug=slug)
        main_cat = Category.objects.get(pk=cat_id)
        parts = Part.objects.filter(sub_category=cat_name)
        sub_cat = Sub_Category.objects.filter(category=Category.objects.get(pk=cat_id))
    
    context = {'cat_name':cat_name, 'parts':parts, 'sub_cats':sub_cat, 'main_cat':main_cat}
    
    return render(request, 'parts_list.html', context)

def parts_detail_view(request, slug):
    part = get_object_or_404(Part, slug=slug)
    
    context = {'part':part}
    
    return render(request, 'part_single.html', context)
