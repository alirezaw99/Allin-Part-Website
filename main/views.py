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

def categories_view(request, slug):
    # title = Category.objects.get(slug=cat_name)
    cat_name = get_object_or_404(Category, slug=slug)  #this throw a 404 if the slug dosn't match the url
    brands = Category.objects.get(id=cat_name.id).brands.all()
    
    parts = Part.objects.filter(category=cat_name)
    
    context = {'cat_name':cat_name,'brands':brands}
    return render(request, 'categories.html', context)

def parts_list_view(request):
    return render(request, 'parts_list.html')

def parts_detail_view(request):
    return render(request, 'part_single.html')
