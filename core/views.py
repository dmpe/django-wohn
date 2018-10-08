from django import forms
from django.shortcuts import *
from django.http import *
from django.core.mail import send_mail
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth.tokens import *
from django.contrib import messages
from django.views import View
# a generic view for creating and saving an object (e.g. user)
from django.views.generic.edit import CreateView
from django.conf import settings
from django.template import *
from django.template.loader import render_to_string
from django.utils.html import *
from django.utils.http import *
from django.utils.encoding import *
from django.urls import reverse
# for messages
from django.utils.safestring import *

################
#######
####### Function based views
#######
################

# HOMEPAGE
def core_index(request):
    return render(request, 'index.html')

# FOOTER
def about(request):
    return render(request, 'about.html')

def privacy(request):
	return render(request, 'privacy.html')

def terms(request):
	return render(request, 'terms.html')

################
#######
####### Class based views
#######
################
class ContactView(View):
	"""
	"""
	contact_template = 'contact.html'

	def post(self, request):
		pass

	def get(self, request)
    	return render(request, self.contact_template)

