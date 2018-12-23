from django import forms
from django.db import *
from django.urls import *

# create a form for our myUser model, for user settings in profile administration
from .models import myUser

# add crispy imports for sending (helper)
from crispy_forms.helper import *
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class RegisterForm(forms.Form):
	"""docstring for RegisterForm
	"""
	inputUsername = forms.CharField(max_length = 30)
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

class FeedbackForm(forms.Form):
	"""docstring for ResetFormStepOne
	"""
	inputFeedback = forms.CharField(widget = forms.Textarea)

class UserProfileForm(forms.ModelForm, RegisterForm):
	"""
	for user profile settings
	"""
	class Meta:
		model = myUser
		fields = ['user_gender']
			