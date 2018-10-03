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
# for messages
from django.utils.safestring import *

import logging

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

# instance of a logger
logger = logging.getLogger(__name__)

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
	This class takes an input from the post request and prepares & sends HTML
	email to the user
	TODO delete gmail
	"""
	template_name = 'reset_password.html'

	def prepare_email(self, request, userPresent_username = None, 
		userPresent_email = None, userPresent_token = None, userPresent_uid = None):

		subject = 'B40.cz: Password Reset'
		from_email = settings.DEFAULT_FROM_EMAIL

		client_headers = http_headers(request)

		cntxt = {"username": userPresent_username, "token": userPresent_token, 
			"password_expire": settings.PASSWORD_RESET_TIMEOUT_DAYS, "uid": userPresent_uid,
			"operating_system": client_headers[0], "ip_address": client_headers[1], 
			"browser": client_headers[2], "browser_version": client_headers[3]}

		html_message = render_to_string('reset_password_email.html', cntxt)
		plain_message = strip_tags(html_message)

		try:
			send_mail(subject, plain_message, from_email, [userPresent_email], html_message=html_message)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')

		return None

	def post(self, request):
		"""
		sends email message to the user's email address
		"""
		inputEmail_Username = request.POST.get('inputEmail_Username', False)
		token_obj = PasswordResetTokenGenerator()

		#check if user is present in the database -> moved to backend
		userPresent = EmailUserNameAuthBackend.check_for_user_existance(self, inputEmail_Username)

		if userPresent[0] is True:
			tk = token_obj.make_token(userPresent[1])
			uid = urlsafe_base64_encode(force_bytes(userPresent[1].pk)).decode()

			self.prepare_email(request, userPresent_username = userPresent[1].get_username(), 
				userPresent_email = "dimitrijenko@gmail.com", 
				userPresent_token= tk, userPresent_uid= uid)

			messages.add_message(request, messages.SUCCESS, 
				mark_safe('<h6 class=''alert-heading''>Password reset was successful!</h6>'
				'<p>Check your email now to set a new one.</p>'
				'<p>You can now <strong>close</strong> this page.</p>'))
		else: 
			messages.add_message(request, messages.ERROR, 
				mark_safe('<h6 class=''alert-heading''>Password reset cannot proceed!</h6>'
				'<p>Check your input as the user cound not be found in the database.</p>'
				'<p>Please, try again.</p>'))

		return render(request, self.template_name)

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class ResetPasswordNewStepTwoView(View):
	"""
	at this stage, a token should have been send to the user via email
	user clicks, inputs passwords and should be able to click and load the main login screen
	"""
	template_name = 'reset_password_new.html'

	def post(self, request, *args, **kwargs):
		inputNewPassword = request.POST.get('inputNewPassword', False)
		inputConfirmNewPassword = request.POST.get('inputConfirmNewPassword', False)
		
		# we dont know who is the user, hence need to fetch
		myuser = validate_password_reset(request)

		if myuser is not None and inputNewPassword == inputConfirmNewPassword:
			my_user.set_password(inputNewPassword)
			my_user.save()

			messages.add_message(request, messages.SUCCESS, 
				'<h6 class=''alert-heading''>Your Password has been changed!</h6>'
				'<p>You can <a href="{% url ''login'' %}" class="alert-link">now login using new credentials on the login page</a>.</p>')
		else:
			messages.add_message(request, messages.WARNING, 
				'<h6 class=''alert-heading''>Two passwords do not match</h6>'
				'<p>Make sure that they are same by checking the capital letters.</p>')

		return render(request, self.template_name)

	def get(self, request, *args, **kwargs):	
		# TODO: should actually display error and not be displayed at all
		# actually this will never be displayed unless full url
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
			# TODO Add message informing user about some error
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