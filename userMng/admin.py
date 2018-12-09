from django import forms
from django.contrib import admin
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import myUser


# class UserCreateForm(UserCreationForm):
# 	"""docstring for UserCreationForm"""

# 	class Meta:
# 		model = myUser
# 		fields = ('username', 'email', 'first_name', 'last_name', 'user_timezone', 'user_int_tel') 
	
# 	def save(self, commit=True):
# 		user = super(UserCreateForm, self).save(commit=False)
# 		user
# 		if commit:
# 			user.save()
# 		return user

class UserAdmin(BaseUserAdmin):
	# add_form = UserCreateForm
	class Meta:
		user = myUser
			
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_timezone', 'user_int_tel')
	
	# fieldsets = (
	# 	(None, {'fields': ('username', 'password')}),
	# 	('Personal info', {'fields': ('first_name', 'last_name', 'user_timezone', 'user_int_tel',)})
	# )

	add_fieldsets = ('Personal info', {'fields': ('user_timezone', 'user_int_tel')})
	

admin.site.register(myUser, UserAdmin)