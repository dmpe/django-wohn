from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bs4(request):
    return HttpResponse("This is another bootstrap 4 page.")