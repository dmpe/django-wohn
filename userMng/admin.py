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
	class Meta:
		model = myUser
		fields = '__all__'

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm
	add_fieldsets = (
		('None', {
			'classes': ('wide',),
			'fields': ('user_timezone', 'user_int_tel')}
		), 
	)

admin.site.register(myUser, UserAdmin)