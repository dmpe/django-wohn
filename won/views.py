from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_profile(request):
    return render(request, 'user_profile.html')
