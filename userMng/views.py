from django import forms
from django.shortcuts import *
from django.http import HttpResponse
from django.core.mail import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.views import View
# a generic view for creating and saving an object (e.g. user)
from django.views.generic.edit import CreateView
from django.conf import settings
from django.template.loader import render_to_string
from django.template import *
from django.utils.html import strip_tags

# used for logout redirect
from core.views import *

# for using not only username/pswd but also email/pswd
from .backends import EmailUserNameAuthBackend

# for registration of users
from .models import myUser

# forms from forms.py file
from .forms import *

# for sending emails with right headers
from .mics import *

################
#######
####### Function based views
#######
################

# ADMINISTRATION
def administrationView(request):
	return render(request, 'administrace/index.html')

def administrationView_UserProfile(request):
	return render(request, 'administrace/user_profile.html')

################
#######
####### Class based views
#######
################


###################################
################
################ Passowrd Reset
################
###################################
class ResetPasswordStepOneView(View):
	"""
	"""
	template_name = 'reset_password.html'

	def prepare_email(self, request, email_to_send= None):
		subject = 'B40.cz: Password Reset'
		from_email = DEFAULT_FROM_EMAIL
		to = self.email_to_send

		client_headers = http_headers(self, request)

		cntxt = {"username": username, "token": "token", 
			"password_expire": PASSWORD_RESET_TIMEOUT_DAYS, 
			"operating_system":client_headers[0], "ip_address":client_headers[1], 
			"browser":client_headers[2], "browser_version":client_headers[3]}

		html_message = render_to_string('reset_password_email.html', cntxt)
		plain_message = strip_tags(html_message)

		try:
			submit.mail(subject, plain_message, from_email, [to], html_message=html_message)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')

	def post(self, request):
		"""
		sends email message to the user's email address
		"""
		inputEmail_Username = request.POST.get('inputEmail_Username', False)
		
		is_valid = valid_email(inputEmail_Username)

		#check if user is present in the database -> moved to backend
		userPresent = EmailUserNameAuthBackend.check_for_existance(inputEmail_Username)

		if userPresent is True:
			if is_valid is True:
				# inputEmail_Username is email
				prepare_email(self, request, email_to_send = "dimitrijenko@gmail.com")
			else:
				# it is username
				prepare_email(self, request, email_to_send = "dimitrijenko@gmail.com")
		else: 
			pass

		return redirect('core_index')

	def get(self, request):
		return render(request, self.template_name)


class ResetPasswordNewStepTwoView(View):
	"""
	at this stage, a token should have been send to the user via email
	user clicks
	"""
	template_name = 'reset_password_new.html'

	def post(self, request):
		pass

	def get(self, request):	
		return render(request, self.template_name)

###################################
################
################ Registration
################
###################################
class RegistrationView(CreateView):
	"""docstring for RegistrationView
	"""
	template_name = 'signup_login/register.html'

	def post(self, request):
		# recieve data from the registration form
		inputUsername = request.POST.get('inputUsername', False)
		inputEmail = request.POST.get('inputEmail', False)
		inputNewPassword = request.POST.get('inputNewPassword', False)
		inputConfirmNewPassword = request.POST.get('inputConfirmNewPassword', False)

		# also validate on the fronend
		if inputNewPassword == inputConfirmNewPassword:
			ur = myUser.objects.create_user(inputUsername, inputEmail)
			ur.set_password(inputNewPassword)
			ur.is_active = True
			ur.save()
		else: 
			pass

		auser = EmailUserNameAuthBackend.authenticate(self, request, username = inputUsername, password = inputNewPassword)

		try:
			django_login(request, auser, backend = 'userMng.backends.EmailUserNameAuthBackend')
			return redirect('userMng_index')
		except Exception as e:
			return redirect(settings.LOGIN_URL)

	def get(self, request):
		# if get request, just render the template, with form
		return render(request, self.template_name)

###################################
################
################ Log In + Log Out
################
###################################
class LoginView(View):
	"""Uses class based view
	"""
	template_name = 'signup_login/login.html'
		
	def post(self, request):
		# recieve
		username_Email = request.POST.get('inputEmail_Username', False)
		user_password = request.POST.get('inputNewPassword', False)
		auth_user = EmailUserNameAuthBackend.authenticate(self, request, username = username_Email, password = user_password)
		
		if auth_user is None:
			# TODO: add some messages via GH #17
			return redirect(settings.LOGIN_URL)
		else: 	
			try:
				# whether the user is active or not is already checked by the 
				# ModelBackend we use
				django_login(request, auth_user, backend = 'userMng.backends.EmailUserNameAuthBackend')
				return redirect('userMng_index')
			except Exception as e:
				raise e

	def get(self, request):
		# if get request just render the template, with form
		return render(request, self.template_name)

class LogoutView(View):
	"""Class based view for logout
	Only requires get method
	"""

	def get(self, request):
		django_logout(request)
		return redirect('core_index')