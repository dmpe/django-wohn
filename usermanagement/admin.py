from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import MyUser

class CustomUserAdmin(UserAdmin):
    model = MyUser

admin.site.register(MyUser) #, CustomUserAdmin)