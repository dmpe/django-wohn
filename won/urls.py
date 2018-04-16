from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bs4', views.bs4, name='bs4'),
]