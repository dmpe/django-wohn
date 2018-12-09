from django import forms
from django.contrib import admin
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import myUser


class UserCreationForm(forms.ModelForm):
	"""docstring for UserCreationForm"""
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = myUser
		fields = ('username', 'email', 'first_name', 'last_name', 'user_timezone', 'user_int_tel') 
	
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class NewUserChangeForm(forms.ModelForm):

	class Meta:
		model = myUser
		fields = ('username', 'email', 'first_name', 'last_name', 'user_timezone', 'user_int_tel') 

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm
	add_fieldsets = (
		('None', {
			'classes': ('wide',),
			'fields': ('username', 'email', 'first_name', 'last_name', 'user_timezone', 'user_int_tel')}
		), 
	)

admin.site.register(myUser, UserAdmin)