from django import forms
from django.contrib import admin
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import myUser

class UserCreatingFormInAdmin(UserCreationForm):
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
		('Personal info', {'fields': ('first_name', 'last_name', 'email', 'user_timezone', 'user_int_tel')}),
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