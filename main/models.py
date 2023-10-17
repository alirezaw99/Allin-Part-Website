from django.db import models

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Auto_Washing_Machine_models(models.Model):
    model_brand = models.OneToOneField(Brands, on_delete=models.SET_NULL, primary_key=False, null=True)
    model_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
class Dishwasher_models(models.Model):
    model_brand = models.OneToOneField(Brands, on_delete=models.SET_NULL, primary_key=False, null=True)
    model_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
class Twin_Washing_Machine_models(models.Model):
    model_brand = models.OneToOneField(Brands, on_delete=models.SET_NULL, primary_key=False, null=True)
    model_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
class Vacuum_Cleaner_models(models.Model):
    model_brand = models.OneToOneField(Brands, on_delete=models.SET_NULL, primary_key=False, null=True)
    model_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
class Refrigerator_models(models.Model):
    model_brand = models.OneToOneField(Brands, on_delete=models.SET_NULL, primary_key=False, null=True)
    model_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
class Accessory_models(models.Model):
    model_brand = models.OneToOneField(Brands, on_delete=models.SET_NULL, primary_key=False, null=True)
    model_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
