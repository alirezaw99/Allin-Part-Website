from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import ContactForm, CommentForm
from django.contrib import messages

# Create your views here.

def home_view(request):
    category = Category.objects.all().order_by('created_date')
    parts = Part.objects.filter(popular=1)
    discounts = Part.objects.filter(is_onsale=1)
    
    context = {'category':category, 'parts':parts, 'discounts':discounts}
    
    return render(request, 'home.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد')
        else:
            messages.error(request, 'پیام شما ثبت نشد! لطفا مجددا تلاش کنید.')
            
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
    images = PartImage.objects.filter(part=part)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.part = part
            comment.save()
            form.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد و در انتظار تایید می باشد.')
        else:
            messages.error(request, 'پیام شما ثبت نشد! لطفا مجددا تلاش کنید.')
            
    comments = Comment.objects.filter(part=part, approved=True)
    
    context = {'part':part, 'images':images, 'comments':comments}
    
    return render(request, 'part_single.html', context)

def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')