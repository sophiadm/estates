#estates URL Configuration
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from manager.sitemaps import SiteMap

sitemaps = {
    'estates': SiteMap()
}

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),

    #url(r'^sitemap.xml/$', map_views.sitemap, {'sitemaps': sitemaps}),

    url(r'', include('manager.urls')),
]
