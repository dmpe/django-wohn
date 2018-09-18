from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# ADMINISTRATION
def index(request):
	return render(request, 'index.html')

def user_profile(request):
    return render(request, 'user_profile.html')

# HEADER - Main Body
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def new_password(request):
	return render(request, 'new_password.html')

def reset_password(request):
	return render(request, 'reset_password.html')

def logout(request):
	return render(request, 'logout.html')
