from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth import *
from core.views import *

# ADMINISTRATION
def userMng_index(request):
	return render(request, 'administrace/index.html')

def user_profile(request):
    return render(request, 'user_profile.html')

# HEADER - Main Body
def register(request):
    return render(request, 'register.html')

def login(request):
	render(request, 'login.html')

	if 'usernameOrEmail' and 'user_password' in request.POST:
		usernameOrEmail = request.POST['inputEmail_Username']
		user_password = request.POST['inputNewPassword']
	else:
    	usernameOrEmail = False
    	user_password = False

	auth_user = authenticate(request, username = usernameOrEmail, password = user_password)

	if auth_user is not None:
		login(request, auth_user)
		return auth_user

def new_password(request):
	return render(request, 'new_password.html')

def reset_password(request):
	return render(request, 'reset_password.html')

def logout(request):
	render(request, 'logout.html')
	logout(request)
	return redirect('core_index')