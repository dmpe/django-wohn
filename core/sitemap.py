from datetime import *

from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# todo automatic generation of sitemaps
# see "that" package on github


class B40_Sitemap(Sitemap):
    """
	B40_Sitemap
	"""

    changeFreq = "monthly"
    priority = 0.6
    lastmod = datetime.now()
    protocol = "https"

    def items(self):
        return ["homepage", "contact", "privacy", "about", "terms"]

    def location(self, item):
        return reverse(item)


class UserMNG_Sitemap(Sitemap):
    """
	create a sitemap for some additional User Management pages
	"""

    changeFreq = "monthly"
    priority = 0.6
    lastmod = datetime.now()
    protocol = "https"

    def items(self):
        return ["register", "login", "reset_password", "userMng_index"]

    def location(self, item):
        return reverse(item)
