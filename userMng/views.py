from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth import *
from core.views import *

# ADMINISTRATION
def userMng_index(request):
	return render(request, 'index.html')

def user_profile(request):
    return render(request, 'user_profile.html')

# HEADER - Main Body
def register(request):
    return render(request, 'register.html')

def login(request):
	usernameOrEmail = request.POST['inputEmail_Username']
	user_password = request.POST['inputNewPassword']
	auth_user = authenticate(request, username = usernameOrEmail, password = user_password)
	if auth_user is not None:
		login(request, auth_user)
		return auth_user

def new_password(request):
	return render(request, 'new_password.html')

def reset_password(request):
	return render(request, 'reset_password.html')

def logout(request):
	logout(request, template_name='logout.html')
	return redirect('core_index')