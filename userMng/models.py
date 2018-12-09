from django.db import *
from django.db import models
from django.contrib.auth.models import *
from django.conf import *

# for storing user's timezone, default is Prague (CET) stored in settings.py
import pytz
from timezone_field import TimeZoneField

# store users phone number
from phonenumber_field.modelfields import PhoneNumberField


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
	# email, username, first and last name are unnecessary
	user_int_tel = PhoneNumberField(blank=True, null=True)
	user_timezone = TimeZoneField(default=settings.TIME_ZONE)
	objects = MyUserManager()
	
	class Meta:
		unique_together = (("email"),)

myUser._meta.get_field('email')._blank = True