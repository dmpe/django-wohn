from . import views
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from userMng.urls import *

app_name = 'core'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
	path('', include('userMng.urls')),

]

