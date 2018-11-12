from . import views
from django.urls import path
from django.conf.urls import include
from django.conf import settings

#app_name = 'core'

urlpatterns = [
    path('', views.core_index, name='core_index'),
    
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    
]

