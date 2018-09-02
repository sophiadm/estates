from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'contact/$', views.contact, name='contact'),
    
    url(r'blog/$', views.blog.home, name='blog'),
    url(r'blog/new/$', views.blog.add, name='blogadd'),
    url(r'blog/(.*)/edit/$', views.blog.edit, name='blogedit'),
    url(r'blog/(.*)/delete/$', views.blog.delete, name='blogdel'),
    url(r'blog/(.*)/$', views.blog.see, name='blogview'),

    url(r'properties/$', views.properties.home, name='propertyhome'),
    url(r'properties/new/$', views.properties.add, name='propertyadd'),
    url(r'properties/(.*)/edit/$', views.properties.edit, name='propertyedit'),
    url(r'properties/(.*)/delete/$', views.properties.delete, name='propertydel'),
    url(r'properties/(.*)/$', views.properties.see, name='propertyview'),

    url(r'reviews/$', views.review.home, name='reviews'),
    url(r'reviews/new/$', views.review.add, name='reviewsadd'),
    url(r'reviews/(.*)/edit/$', views.review.edit, name='reviewsedit'),
    url(r'reviews/(.*)/delete/$', views.review.delete, name='reviewsdel'),

    url(r'faqs/$', views.qanda.home, name='faqs'),
    url(r'faqs/new/$', views.qanda.add, name='faqsadd'),
    url(r'faqs/(.*)/edit/$', views.qanda.edit, name='faqsedit'),
    url(r'faqs/(.*)/delete/$', views.qanda.delete, name='faqsdel'),

    url(r'^.*/$', views.no_match)
]
