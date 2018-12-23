from django.db import *
from django.db import models
from django.contrib.auth.models import *
from django.conf import *
from django_countries.fields import *

# for storing user's timezone, default is Prague (CET) stored in settings.py
import pytz
from timezone_field import TimeZoneField

# store users phone number
from phonenumber_field.modelfields import PhoneNumberField

class MyUserManager(UserManager):
    pass

class myUser(AbstractUser):
	# email, username, first and last name are unnecessary
	GENDER_CHOICES = (
		('M', 'Mr.'),
		('F', 'Mrs. or Miss'),
	)
	user_gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
	user_int_tel = PhoneNumberField(blank=True, null=True)
	user_timezone = TimeZoneField(default=settings.TIME_ZONE)
	country = CountryField(blank=True)
	objects = MyUserManager()
	
	class Meta:
		unique_together = (("email"),)

class UserMessage(models.Model):
	"""
	For private communication.
	https://stackoverflow.com/questions/35310283/how-to-model-messages-exchanged-between-users-er-diagram
	"""
	send_date = models.TimeField(auto_now_add=True) # will not display
	from_whom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="from_whom_user", on_delete=models.CASCADE)
	to_whom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="to_whom_user", on_delete=models.CASCADE)
	inputMessage = models.TextField()