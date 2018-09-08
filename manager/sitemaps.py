from django.contrib.sitemaps import Sitemap
from .models import BlogPost, Property
from django.urls import reverse

class StaticSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        mylist = ['home', 'about', 'blog', 'faqs', 'reviews', 'contact']
        if [1 for p in Property.objects.all() if p.available]:
            mylist.append('propertyhome')
            
        return mylist

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




