from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import myUser


# class UserCreationForm(forms.ModelForm):
# 	"""docstring for UserCreationForm"""
# 	model = myUser
# 	fields = ('user_timezone', 'user_int_tel')

class UserAdmin(BaseUserAdmin):
	model = myUser
	filter_horizontal = ('user_timezone', 'user_int_tel')
	
admin.site.register(myUser, UserAdmin)