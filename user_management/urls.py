from . import views
from django.urls import path

urlpatterns = [  
    path('user_profile', views.user_profile, name='user_profile'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('new_password', views.new_password, name='new_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    url('', include('social_django.urls', namespace='social'))
    
]