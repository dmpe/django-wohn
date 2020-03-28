from django import forms
from django.db import *
from django.urls import *
from django_countries.widgets import *

from .models import *


class RegisterForm(forms.Form):
    """
	docstring for RegisterForm
	"""

    inputUsername = forms.CharField(max_length=30)
    inputEmail = forms.EmailField(widget=forms.EmailInput())
    inputNewPassword = forms.CharField(widget=forms.PasswordInput())
    inputConfirmNewPassword = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    """
	Users can login either via username or email.
	Hence, input type="text"
	"""

    inputEmail_Username = forms.CharField(widget=forms.TextInput())
    inputNewPassword = forms.CharField(widget=forms.PasswordInput())


class ResetFormStepOne(forms.Form):
    """docstring for ResetFormStepOne
	"""

    inputEmail_Username = forms.CharField(widget=forms.TextInput())


