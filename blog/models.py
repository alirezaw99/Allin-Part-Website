from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.tag

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.BooleanField()
    image = models.ImageField(upload_to='blog/')
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    eddited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    