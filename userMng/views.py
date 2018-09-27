from django.shortcuts import *
from django.http import HttpResponse
from django import forms
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.views import View
from django.conf import settings

# a generic view for creating and saving an object (e.g. user)
from django.views.generic.edit import CreateView

from core.views import *

# for using not only username/pswd but also email/pswd
from .backend import EmailUserNameAuthBackend

# ADMINISTRATION
def userMng_index(request):
	return render(request, 'administrace/index.html')

def user_profile(request):
    return render(request, 'user_profile.html')

# HEADER - Main Body
class RegistrationView(CreateView):
	"""docstring for RegistrationView
	"""
	template_name = 'signup_login/register.html'

	def get(self, request):
		return render(request, self.template_name)

class LoginView(View):
	"""Uses class based view
	"""
	template_name = 'signup_login/login.html'
		
	def post(self, request):
		pass
		#if 'usernameOrEmail' and 'user_password' in request.POST:
		# 	usernameOrEmail = request.POST['inputEmail_Username']
		# 	user_password = request.POST['inputNewPassword']
		#else:
		# 	usernameOrEmail = False
		# 	user_password = False

		#auth_user = authenticate(request, username = usernameOrEmail, password = user_password)

		#if auth_user is not None:
		# 	django_login(request, auth_user)
		 	#return auth_user
		#else:
		#	return redirect(settings.LOGIN_URL)

	def get(self, request):
		# if get request just render the template
		return render(request, self.template_name)

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