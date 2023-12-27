from django.contrib import sitemaps
from django.db.models.base import Model
from django.urls import reverse
from .models import Part, Category, Sub_Category


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "never"

    def items(self):
        return ["main:home","main:about", "main:contact"]

    def location(self, item):
        return reverse(item)
    
class CategorySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "never"

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse("main:categories", kwargs={"slug": item.slug})

class SubCategorySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "never"

    def items(self):
        return Sub_Category.objects.all()

    def location(self, item):
        return reverse("main:categories", kwargs={"slug": item.slug})
    
class PartSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return Part.objects.all()
    
    def location(self, item):
        return reverse("main:part_detail", kwargs={"slug": item.slug})