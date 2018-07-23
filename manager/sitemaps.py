from django.contrib.sitemaps import Sitemap
from .models import BlogPost

class SiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()
