from .models import Category, Sub_Category

def base_context(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    
    return {'category':category, 'sub_category':sub_category}