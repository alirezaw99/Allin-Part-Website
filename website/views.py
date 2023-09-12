from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, 'Front\index.html')

def contact_view(request):
    return HttpResponse('<h1>This is Contact Page</h1>')
