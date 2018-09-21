from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# HOMEPAGE
def core_index(request):
    return render(request, 'index.html')

# FOOTER
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
	return render(request, 'privacy.html')

def terms(request):
	return render(request, 'terms.html')