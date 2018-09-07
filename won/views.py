from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def new_password(request):
	return render(request, 'new_password.html')

def reset_password(request):
	return render(request, 'reset_password.html')