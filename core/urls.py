from . import views
from django.urls import path

urlpatterns = [
    path('', views.core_index, name='core_index'),
    
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    
]