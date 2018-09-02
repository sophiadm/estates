from django.contrib.sitemaps import Sitemap
from .models import BlogPost, Property
from django.urls import reverse

class StaticSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'blog', 'faqs', 'reviews', 'contact']

    def location(self, item):
        return reverse(item)

class BlogSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()
    
class PropertySiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Property.objects.filter(available=True)




