from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def blog_home_view(request):
    posts = get_list_or_404(Blog, publish=True)
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog_home.html', {'page_obj':page_obj})


def blog_single_view(request, id):
    all_posts = Blog.objects.all().order_by('-created_date')[:5]
    all_tags = get_list_or_404(Tag)
    
    post = get_object_or_404(Blog, id=id)
    tags = post.tags.all()

    context = {'post':post, 'tags':tags, 'all_tags':all_tags, 'all_posts':all_posts}
    return render(request , 'blog_single.html', context)


def blog_category_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Blog.objects.filter(tags=tag, publish=True
                                )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog_tag.html', {'page_obj':page_obj, 'tag':tag})
    
    