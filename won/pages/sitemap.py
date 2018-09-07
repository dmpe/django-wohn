from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from datetime import *

class B40_Sitemap(Sitemap):
    """docstring for B40_Sitemap
    """
    changeFreq = "monthly"
    priority = 0.6
	lastmod = datetime.now()
	protocol = "https"

    def items(self):
    	return ['index', 'contact', 'privacy', 'about', 'terms']

    def location(self, item):
    	return reverse(item)