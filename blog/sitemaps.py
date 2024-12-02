from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = "weekly"  # Indicates the frequency of changes
    priority = 0.8         # Relative importance of this URL

    def items(self):
        """Return the queryset of blog posts."""
        return Blog.objects.filter(publish=True)

    def lastmod(self, obj):
        """Return the last modified date for each post."""
        return obj.eddited_date  # Replace with the field tracking updates
