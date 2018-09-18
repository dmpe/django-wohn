from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings

class MyUserManager(UserManager):
    pass

"""
Define what users can do/have:
user_created = uses timestamp (mutually exclusive with default=timezone.now())
user_name = short name
def __str__(self):
return '{} ({})'.format(get_username(),  get_email_field_name())
"""
class myUser(AbstractUser):
	user_first_name = models.CharField(max_length = 200)
	user_last_name = models.CharField(max_length = 200)
	user_int_tel = PhoneNumberField(blank=True)
	objects = MyUserManager()

	#def __str__(self):
	#	return '{} ({})'.format(request.user.username,  request.user.email)