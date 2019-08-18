from django import forms
from django.db import *
from django.urls import *
from django_countries.widgets import *

from core.forms import RegisterForm
from core.models import *


class FeedbackForm(forms.Form):
	"""docstring for ResetFormStepOne
	"""
	inputFeedback = forms.CharField(widget = forms.Textarea)

class NewPropertyForm(forms.ModelForm):
	"""
	Form for adding new properties
	"""

	class Meta:
		model = Property
		fields = '__all__'

class UserProfileForm(forms.ModelForm, RegisterForm):
	"""
	for user profile settings
	"""
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['user_gender'].label = "Select your gender"
		self.fields['first_name'].label = "First Name"
		self.fields['last_name'].label = "Last Name"
		self.fields['user_first_lastname_visibility'].label = "Publically visible name"
		self.fields['user_units_system'].label = "Imperial or Metric"
		self.fields['user_timezone'].label = "Timezone"
		self.fields['user_country'].label = "Country"
		self.fields['user_int_tel'].label = "Phone number"

		self.fields['inputUsername'].label = "New username"
		self.fields['inputEmail'].label = "New email"
		self.fields['inputNewPassword'].label = "New Password"
		self.fields['inputConfirmNewPassword'].label = "Confirm new password"

	class Meta:
		model = myUser
		fields = ['user_gender', 'first_name', 'last_name', 'user_first_lastname_visibility',
			'user_units_system', 'user_timezone', 'user_country', 
			'user_int_tel', 'inputUsername', 'inputEmail', 
			'inputNewPassword', 'inputConfirmNewPassword']
