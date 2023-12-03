from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact_us.html')

def about_view(request):
    return render(request, 'about_us.html')

def categories_view(request, cat_name):
    context = {str(cat_name):'sdf'}
    return render(request, 'categories.html', context)

def parts_list_view(request):
    return render(request, 'parts_list.html')

def parts_detail_view(request):
    return render(request, 'part_single.html')
