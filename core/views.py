from django import forms
from django.shortcuts import *
from django.http import *
from django.core.mail import send_mail
from django.contrib import messages
from django.views import View
from django.conf import settings
from django.template import *
from django.template.loader import render_to_string
from django.utils.html import *
from django.utils.http import *
from django.utils.encoding import *
from django.urls import *
# for messages
from django.utils.safestring import *

from .forms import *

from userMng.mics import *

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
	Contact Form using Django approach to constructing
	forms.
	"""
	template_name = 'contact.html'

	def post(self, request):
		form = ContactForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['inputName']
			email = form.cleaned_data['inputEmail']
			subject = form.cleaned_data['inputSubject']
			text_msg = form.cleaned_data['inputText']
			recap_token = request.POST.get('g-recaptcha-response', False)
		
			if is_human(recap_token) is True:

				prepare_visitor_mssg_email(request, username, email, subject, text_msg)

				messages.add_message(request, messages.SUCCESS, 
					mark_safe('<h6 class=''alert-heading''>Thank you for sending us the message!</h6>'
					'<p>We wiill respond to you <strong>as soon as possible</strong>.</p>'))
			else:
				messages.add_message(request, messages.WARNING, 
						mark_safe('<h6 class=''alert-heading''>Sorry, but you seem to be a computer bot.</h6>'
						'<p>Please resend the message again, clean cookies or click on the left to email us directly.</p>'))
		else:
			messages.add_message(request, messages.ERROR, 
				mark_safe('<h6 class=''alert-heading''>You message does not fulfill our basic requirenements!</h6>'
				'<p>Check that all fields are filled correctly.</p>'))

		return render(request, self.template_name, {"form": form })	

	def get(self, request):
		form = ContactForm()
		return render(request, self.template_name, {"form": form })

