from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, './home.html')

def contact_view(request):
    return render(request, './contact_us.html')

def about_view(request):
    return render(request, './about_us.html')

