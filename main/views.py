from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact_us.html')

def about_view(request):
    return render(request, 'about_us.html')

def categories_view(request, cat_name):
    # title = Category.objects.get(slug=cat_name)
    title = get_object_or_404(Category, slug=cat_name)  #this throw a 404 if the slug dosn't match the url
    context = {'cat_name':title}
    return render(request, 'categories.html', context)

def parts_list_view(request):
    return render(request, 'parts_list.html')

def parts_detail_view(request):
    return render(request, 'part_single.html')
