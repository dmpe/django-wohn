from crispy_forms.bootstrap import *
from crispy_forms.helper import *
from crispy_forms.layout import *
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


class ContactForm(forms.Form):
    """
	Keep this as cripsy form !
	"""

    SubjectHeadlineChoice = (
        ("general", "General Questions"),
        ("ads", "Advertising"),
        ("com_abs_similar", "Compaints/Abuse"),
        ("help_me", "Help me with something"),
    )

    inputName = forms.CharField(required=True, label="Name", max_length=30)
    inputEmail = forms.EmailField(label="Email", required=True, widget=forms.EmailInput())
    inputSubject = forms.ChoiceField(label="Message deals with...", required=True, choices=SubjectHeadlineChoice)
    # we can have more than 255 chars in the message, hence TextField
    # and not CharField
    inputText = forms.CharField(label="Your message is about....", widget=forms.Textarea, required=True)
