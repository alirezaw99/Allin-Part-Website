from django.db import models
from .misc import get_upload_path

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
    slug = models.SlugField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f'{self.name_fa} {self.category}'
    
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
    used_models = models.ManyToManyField(Model)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=get_upload_path, default='images/default.png')
    description = models.TextField(null=True, blank=True)
    in_stock = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)
    discoundet_price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default="", null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name