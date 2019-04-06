from . import views
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from pinax.messages import *
# from core.urls import *

# app_name = 'userMng'
# https://stackoverflow.com/questions/49655525/django-2-0-not-a-valid-view-function-or-pattern-name-customizing-auth-views

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name='register'),
    
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    
    path('reset_password', views.ResetPasswordStepOneView.as_view(), name='reset_password'),
    path('new_password/<uidb64>/<token>/', views.ResetPasswordNewStepTwoView.as_view(), name='new_password'),
    
    # not in the Sitemap
	path('administrace/', views.UserProfileIndex.as_view(), name='userMng_index'),    
    path('administrace/profile', views.UserProfileAdministration.as_view(), name='user_profile'), 
    path('administrace/properties', views.UserProfileProperties.as_view(), name='user_properties'),
    path('administrace/messages/', include("pinax.messages.urls", namespace="pinax_messages")),

    path('administrace/my_property_ads', views.AdvertisingMyAdd.as_view(), name='my_property_ads'),
    path('administrace/ad_statistics', views.AdvertisingStatistics.as_view(), name='ad_statistics'),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('core.urls')),
]

