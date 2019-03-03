"""vanoce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps import views
from django.contrib.sitemaps.views import sitemap
from django.urls import *
from django.views.generic import TemplateView
from django.conf.urls import url

from core import views
from core.sitemap import B40_Sitemap, UserMNG_Sitemap
from userMng import views

sitemaps = {
    'core': B40_Sitemap,
    'userMng': UserMNG_Sitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('core.urls')),
    path('', include('userMng.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
