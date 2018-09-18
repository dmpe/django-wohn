from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    
]