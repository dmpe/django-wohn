from . import views
from django.urls import path
from django.conf.urls import include
from django.conf import settings

#app_name = 'userMng'
# https://stackoverflow.com/questions/49655525/django-2-0-not-a-valid-view-function-or-pattern-name-customizing-auth-views

urlpatterns = [  
    path('register', views.RegistrationView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('reset_password', views.ResetPasswordStepOneView.as_view(), name='reset_password'),
    path('new_password/<uidb64>/<token>/', views.ResetPasswordNewStepTwoView.as_view(), name='new_password'),
    
    # largely should not be in the Sitemap
    path('administrace/user_profile', views.administrationView_UserProfile, name='user_profile'),
	path('administrace/', views.administrationView, name='userMng_index'),    

    path('oauth/', include('social_django.urls', namespace='social')),
]

