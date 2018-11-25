from django import forms
from django.db import *
from django.core.exceptions import *
from django.shortcuts import *
from django.http import *
from django.core.mail import send_mail
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth.tokens import *
from django.contrib.auth.decorators import *
from django.contrib.auth.mixins import *
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
import logging
logger = logging.getLogger(__name__)

################
#######
####### Function based views
#######
################

################
#######
####### Class based views
#######
################

###########################################
#######
####### User Profile Administration / Listing of properties
#######
###########################################
class UserProfileIndex(LoginRequiredMixin, View):
	"""
	The homepage of the administration - the essential Dashboard for the User
	Used for displaing information and submitting new feature requests
	"""
	
	template_name = "user_adm_index.html"

	def post(self, request):
		form = FeedbackForm(request.POST)

		if form.is_valid():
			feedback = form.cleaned_data['inputFeedback']

			prepare_visitor_mssg_email(request, userPresent_username = request.user.get_username(), userPresent_email = request.user.email, subject="User's Feedback: ", text_msg = feedback)

			messages.add_message(request, messages.SUCCESS, 
				mark_safe('<h6 class=''alert-heading''>Thank you for sending us the message!</h6>'
					'<p>We wiill respond to you <strong>as soon as possible</strong>.</p>'))
		else:
			messages.add_message(request, messages.ERROR, 
				mark_safe('<h6 class=''alert-heading''>You message does not fulfill our basic requirenements!</h6>'
				'<p>Check that all fields are filled correctly.</p>'))

		return render(request, self.template_name, {"form": form })	

	def get(self, request):
		"""docstring for get
		"""
		form = FeedbackForm()
		return render(request, self.template_name, {"form": form })

class UserProfileAdministration(LoginRequiredMixin, View):
	"""
	The homepage for user profile - where the settings can be changed
	"""
	
	template_name = "user_profile.html"
	
	def post(self, request):
		"""docstring for post
		"""
		pass
	
	def get(self, request):
		"""docstring for get
		"""
		return render(request, self.template_name)
		
class UserProfileProperties(LoginRequiredMixin, View):
	"""
	The homepage for user's properties - their list and small dashboard
	"""
	
	template_name = "user_property.html"
	
	def post(self, request):
		"""docstring for post
		"""
		pass
	
	def get(self, request):
		"""docstring for get
		"""
		return render(request, self.template_name)

class UserProfileMessages(LoginRequiredMixin, View):
	"""docstring for UserProfileMessages"""
	template_name = "user_messages.html"
	
	def post(self, request):
		"""docstring for post
		"""
		pass
	
	def get(self, request):
		"""docstring for get
		"""
		return render(request, self.template_name)


###################################
################
################ Passoword Reset
################
###################################
class ResetPasswordStepOneView(View):
	"""
	This class takes an input from the post request and prepares & sends HTML
	email to the user
	"""
	template_name = 'reset_password.html'

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

			prepare_psswd_reset_email(request, 
				userPresent_username = userPresent[1].get_username(), 
				userPresent_email = userPresent[1].email, 
				userPresent_token= tk, 
				userPresent_uid= uid)

			messages.add_message(request, messages.SUCCESS, 
				mark_safe('<h4 class=''alert-heading''>Password reset was successful!</h4>'
				'<p>Check your email now to set a new one.</p>'
				'<p>You can now <strong>close</strong> this page.</p>'))
		else: 
			messages.add_message(request, messages.ERROR, 
				mark_safe('<h4 class=''alert-heading''>Password reset cannot proceed!</h4>'
				'<p>Check your input as the user cound not be found in the database.</p>'
				'<p>Please, try again.</p>'))

		return render(request, self.template_name)

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class ResetPasswordNewStepTwoView(View):
	"""
	at this stage, a token should have been send to the user via email
	user clicks, inputs passwords, confirms and he should be able to load the main login screen
	"""
	template_name = 'reset_password_new.html'

	def post(self, request, *args, **kwargs):
		inputNewPassword = request.POST.get('inputNewPassword', False)
		inputConfirmNewPassword = request.POST.get('inputConfirmNewPassword', False)
		
		# we dont know who is the user, hence need to fetch from the URL
		myuser = validate_password_reset(request)

		if myuser is not None and inputNewPassword == inputConfirmNewPassword:
			myuser.set_password(inputNewPassword)
			myuser.save()

			messages.add_message(request, messages.SUCCESS, 
				format_html(('<h4 class=''alert-heading''>Your Password has been changed!</h4>'
				'<p>You can <a href="{}" class="alert-link">now login using new credentials on the login page</a>.</p>'), reverse('login')))
		else:
			messages.add_message(request, messages.WARNING, 
				mark_safe('<h4 class=''alert-heading''>New passwords do not match</h4>'
				'<p>Make sure that they are same, e.g. by checking the capital letters.</p>'))

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

	def post(self, request, *args, **kwargs):
		# recieve data from the registration form
		inputUsername = request.POST.get('inputUsername', False)
		inputEmail = request.POST.get('inputEmail', False)
		inputNewPassword = request.POST.get('inputNewPassword', False)
		inputConfirmNewPassword = request.POST.get('inputConfirmNewPassword', False)
		

		if inputNewPassword == inputConfirmNewPassword:
			try:
				ur = myUser.objects.create_user(inputUsername, inputEmail)
				ur.set_password(inputNewPassword)
				ur.is_active = True
				ur.save()
			except (IndexError, IntegrityError, ValidationError) as e:
				messages.add_message(request, messages.WARNING, 
					format_html(('<h4 class=''alert-heading''>Username or Email already exist</h4>'
					'<p>It seems that your username and/or email already exist in our system.</p>'
					'<p>You can reset <a class = ''alert-link'' href="{}">your password</a> or provide again a unique combination of username & email.</p>'), reverse('reset_password')))
				
				return render(request, self.template_name)
		else: 
			messages.add_message(request, messages.WARNING, 
				mark_safe('<h4 class=''alert-heading''>New passwords do not match</h4>'
				'<p>Make sure that they are same, e.g. by checking the capital letters.</p>'))
				
			return render(request, self.template_name)
			
		auser = EmailUserNameAuthBackend.authenticate(self, request, username = inputUsername, password = inputNewPassword)

		try:
			django_login(request, auser, backend = 'userMng.backends.EmailUserNameAuthBackend')
			return redirect('userMng_index')
		except Exception as e:
			return redirect(settings.LOGIN_URL)

	def get(self, request, *args, **kwargs):
		# if get request, just render the template, with form
		return render(request, self.template_name)

###################################
################
################ Log In + Log Out
################
###################################
class LoginView(View):
	"""
	Uses class based view
	"""
	template_name = 'signup_login/login.html'
		
	def post(self, request, *args, **kwargs):
		# recieve
		username_email = request.POST.get('inputEmail_Username', False)
		user_password = request.POST.get('inputNewPassword', False)
		recap_token = request.POST.get('g-recaptcha-response', False)
		print(recap_token)

		if is_human(recap_token):
			try:
				auth_user = EmailUserNameAuthBackend.authenticate(self, request, username = username_email, password = user_password)
				
				if auth_user is None:
					messages.add_message(request, messages.WARNING, 
						mark_safe('<h4 class=''alert-heading''>Such a user does not exist.</h4>'
						'<p>Make sure that username and password are correct.</p>'))
				else: 	
					try:
						# whether the user is active or not is already checked by the 
						# ModelBackend we use
						django_login(request, auth_user, backend = 'userMng.backends.EmailUserNameAuthBackend')
						return redirect(request.POST.get('next','userMng_index'))
					except Exception as e:
						raise e

			except Exception as e:
				raise e
		# user is bot
		else:
			messages.add_message(request, messages.WARNING, 
						mark_safe('<h4 class=''alert-heading''>Sorry, but you seem to be a computer bot.</h4>'
						'<p>Please contact us if you believe you were wrongly identified because of Google Recaptha v3.</p>'
						'<p>Solution: clear your cookies and try again.</p>'))
		
		return render(request, self.template_name)

	def get(self, request, *args, **kwargs):
		# if get request just render the template, with form
		return render(request, self.template_name)

class LogoutView(View):
	"""
	Class based view for logout
	Only requires get method
	"""
	def get(self, request):
		django_logout(request)
		return redirect('core_index')