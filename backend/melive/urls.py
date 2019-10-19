"""melive URL Configuration

The `urlpatterns` list routes URLs to views.

See:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/

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
import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

from core.sitemap import B40_Sitemap, UserMNG_Sitemap

sitemaps = {"core": B40_Sitemap, "userMng": UserMNG_Sitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("userMng.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),
    path(
        "administrace/messages/",
        include("pinax.messages.urls", namespace="pinax_messages"),
    ),
    url(
        r"^robots.txt$",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots_file",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('__debug__/', include(debug_toolbar.urls)),
    # expose graphql server api, incl. GraphQL IDE - and
    # disable CSRF token requirement because for now it is PUBLIC API
    # TODO it should be protected
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
