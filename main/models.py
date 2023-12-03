from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
  
class Auto_Washing_Machine_Model(models.Model):
    model_brand = models.OneToOneField(Brand, on_delete=models.SET_NULL, null=True)
    model_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.model_brand} - {self.model_name}"
    
class Auto_Washing_Machine_Part(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=15)
    used_models = models.ForeignKey(Auto_Washing_Machine_Model, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()
    #picture = models.ImageField()
    description = models.TextField(null=True)
    in_stock = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)
    discounted_price = models.PositiveIntegerField(default=0)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    