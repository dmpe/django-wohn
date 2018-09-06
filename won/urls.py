from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('register', views.register, name='register'),
]