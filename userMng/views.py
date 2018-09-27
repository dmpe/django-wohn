from django.shortcuts import *
from django.http import HttpResponse
from django import forms
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.views import View
from django.conf import settings

# a generic view for creating and saving an object (e.g. user)
from django.views.generic.edit import CreateView

# used for logout redirect
from core.views import *

# for using not only username/pswd but also email/pswd
from .backends import EmailUserNameAuthBackend

# for registration of users
from .models import myUser

# forms from forms.py file
from .forms import *

# ADMINISTRATION
class AdministrationView(View):
	"""
	"""

	def get(self, request):
		return render(request, 'administrace/index.html')

class Adminisration_UserProfile(View):
	"""docstring for Adminisration_UserProfile
	"""
	
	def get(self, request):
		return render(request, 'administrace/user_profile.html')

# HEADER - Main Body
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

		##if inputNewPassword == inputConfirmNewPassword:
		ur = myUser.objects.create_user(inputUsername, inputEmail)
		ur.set_password(inputNewPassword)
		ur.is_active = True
		ur.save()

		#auser = EmailUserNameAuthBackend.authenticate(self, request, username = inputUsername, password = inputNewPassword)
			
		#try:
		#	django_login(request, auser)
		#except ValueError:
		#	return redirect(settings.LOGIN_URL)

		return AdministrationView.as_view()(request)

		#else:
		#	return redirect('/')


	def get(self, request):
		# if get request just render the template, with form
		myRegistrationForm = RegisterForm()
		return render(request, self.template_name, {'form': myRegistrationForm})

class LoginView(View):
	"""Uses class based view
	"""
	template_name = 'signup_login/login.html'
		
	def post(self, request):
		# recieve
		username_Email = request.POST.get('inputEmail_Username', False)
		user_password = request.POST.get('inputNewPassword', False)
		
		# also try with self
		auth_user = EmailUserNameAuthBackend.authenticate(self, request, username = username_Email, password = user_password)

		if auth_user is not None:
			# whether the user is active or not is already checked by the 
			# ModelBackend we use
			django_login(request, auth_user, backend='userMng.backends.EmailUserNameAuthBackend')
			return AdministrationView.as_view()
		else:
			# TODO: add some messages via GH #17
			return redirect(settings.LOGIN_URL)

		return render(request, self.template_name)

	def get(self, request):
		# if get request just render the template, with form
		myLoginForm = LoginForm()
		return render(request, self.template_name, {'form' : myLoginForm})

def new_password(request):
	return render(request, 'new_password.html')

def reset_password(request):
	return render(request, 'reset_password.html')

class LogoutView(View):
	"""Class based view for logout
	Only requires get method
	"""

	def get(self, request):
		django_logout(request)
		return redirect('core_index')