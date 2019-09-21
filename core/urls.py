from django.conf import settings
from django.conf.urls import include
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),

    path('register', views.RegistrationView.as_view(), name='register'),

    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),

    path('reset_password', views.ResetPasswordStepOneView.as_view(), name='reset_password'),
    path('new_password/<uidb64>/<token>/', views.ResetPasswordNewStepTwoView.as_view(), name='new_password'),
    path('oauth/', include('social_django.urls', namespace='social')),

]
