from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [  
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.login, name='logout'),
    path('new_password', views.new_password, name='new_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('index', views.index, name='index'),
    path('oauth/', include('social_django.urls', namespace='social'))    
]