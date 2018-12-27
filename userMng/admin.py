from django import forms
from django.contrib import admin
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import *

class UserMessageAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

class UserCreatingFormInAdmin(UserCreationForm):
	"""
	By default, email is not added to the registration form
	and thus hacking is required:
	https://stackoverflow.com/a/48605586/2171456

	We extend here that user registration. 
	"""
	email = forms.EmailField(required=True)

	class Meta:
		model = myUser
		fields = ('username', 'password1', 'password2', 'email')	
		
	def __init__(self, *args, **kwargs):
		super(UserCreatingFormInAdmin, self).__init__(*args, **kwargs)
	
	def save(self, commit=True):
		user = super(UserCreatingFormInAdmin, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class UserAdmin(BaseUserAdmin):
	add_form = UserCreatingFormInAdmin

	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal info', {'fields': ('user_gender', 'first_name', 'last_name', 'email', 'user_timezone', 'user_int_tel', 
			'country', 'user_first_lastname_visibility', 'user_units_system')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')})
	)

	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_timezone', 'user_int_tel')

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'password1', 'password2', 'email')}
		),
	)

admin.site.register(myUser, UserAdmin)
admin.site.register(UserMessage, UserMessageAdmin)