from django.db import models
from .misc import get_tumbnail_upload_path , get_images_upload_path

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='category_icons', default='images/default.png')
    slug = models.SlugField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name_fa
    
class Sub_Category(models.Model):
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='category_icons', default='images/default.png')
    slug = models.SlugField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f' {self.category} / {self.name_fa}'
    
class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Part(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=15, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    used_models = models.CharField(max_length=255, null=True)
    price = models.PositiveIntegerField()
    image_tumbnail = models.ImageField(upload_to=get_tumbnail_upload_path, default='images/default.png', blank=True)
    description = models.TextField(null=True, blank=True)
    popular = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)
    discounted_price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default="", null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class PartImage(models.Model):
    part = models.ForeignKey(Part, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_images_upload_path, default='images/default.png')
    
    def __str__(self):
        return self.part.name 
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email  = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name