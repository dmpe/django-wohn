from . import views
from django.urls import path
from django.conf.urls import include

#app_name = 'userMng'

urlpatterns = [  
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('new_password', views.new_password, name='new_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    
    path('administrace/user_profile', views.user_profile, name='user_profile'),
    path('administrace/', views.userMng_index, name='userMng_index'),
    
    path('oauth/', include('social_django.urls', namespace='social')),
]

