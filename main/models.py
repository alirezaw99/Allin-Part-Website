from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name_fa = models.CharField(max_length=255, default='none')
    name_en = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name_fa

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
  
class Model(models.Model):
    model_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.model_brand} - {self.model_name}"
    
class Part(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=15)
    used_models = models.ManyToManyField(Model)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    #picture = models.ImageField()
    description = models.TextField(null=True)
    in_stock = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)
    discounted_price = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    