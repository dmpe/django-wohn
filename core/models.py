import hashlib
import os
# for gravatar URLs and user's profile image and its unique name
import urllib
import uuid

# for time related tasks, incl. timezone
import pytz
from django.conf import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import *
from django.db import *
from django.utils.safestring import *
from django_countries.fields import *
from phonenumber_field.modelfields import *
from timezone_field import *

from .mics import *


class Property(models.Model):
	"""
	Define each apartment, 1-to-n with Users
	unit conversion --> https://pint.readthedocs.io/en/latest/
	"""
	property_created = models.DateTimeField(auto_now_add = True) # will not display

	property_offered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	# Characteristics for each house and apartment
	property_rooms = models.IntegerField()
	# do not delete because part of US/Metric if else switch
	property_size_in_sq_meters = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True)
	property_size_in_sq_foot = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True) 
	# used for calculated prices, same principle
	property_price_in_eur = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True) 
	property_price_in_czk = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True) 
	property_price_in_usd = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True) 

	class Meta:
		verbose_name_plural = "properties"

	def calculate_eur_czk():
		"""
		TODO
		From eur to CZK
		"""
		exr_rat = ExchangeRate.objects.last()
		return exr_rat

class ExchangeRate(models.Model):
	"""
	parse_forex_data in misc.py
	Q: are we going to calculate forex dynamically via JS or we need to
	store all there pairs. Does user have the capability to put 
	different number ?
	"""
	today = models.DateField("Today's Date", auto_now_add=True) # will not display
	OneEurCzk = models.DecimalField("1 EUR - CZK", max_digits=7, decimal_places=3)
	OneEurUsd = models.DecimalField("1 EUR - USD", max_digits=7, decimal_places=3)
	OneUsdCzk = models.DecimalField("1 USD - CZK", max_digits=7, decimal_places=3)
	
class MyUserManager(UserManager):

	def return_profile_image(self, email):
		"""
		This functions takes user_profile_image = models.ImageField and adds gravatar logic to it as well
		1 fetch "user uploaded pictire", if none then use gravatar function
		"""
		pass		
		# if():
		# 	avatar_profile = 
		# else:
		# 	avatar_profile = fetch_gravatar(email=email)
		# return avatar_profile

	def fetch_gravatar(self, email, default = "https://via.placeholder.com/150"):
		"""
		fetching gravatar image
		https://en.gravatar.com/site/implement/images/python/
		If none is found to be associated with the email adress, then default image is used
		"""
		size = 20
		gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?"
		gravatar_url += urllib.parse.urlencode({'d':default, 's':str(size)})

		return gravatar_url

	def fetch_owners_properties_count(self, user_id):
		property_owner = myUser.objects.filter(pk=user_id).first()
		property_count = Property.objects.filter(property_offered_by = property_owner).count()
		print(property_count)

		return property_count

class myUser(AbstractUser):
	# email, username, first and last name are unnecessary
	GENDER_CHOICES = (
		('M', 'Mr.'),
		('F', 'Mrs. or Miss'),
		('O', 'Other or prefer not to say')
	)
	user_gender = models.CharField(max_length=1, choices = GENDER_CHOICES, null = True, default = "O")
	user_int_tel = PhoneNumberField(blank = True, null = True)
	user_timezone = TimeZoneField(default = settings.TIME_ZONE)
	user_country = CountryField(default = "CZ")
	
	# using a function here 
	user_profile_image = models.ImageField(upload_to = upload_profile_image, blank = True,
		null = True)
	
	UNITS_SYSTEM = (
		('Imperial', 'Imperial'),
		('Metric', 'Metric'),
	)
	user_units_system = models.CharField(max_length=10, choices = UNITS_SYSTEM, null = True, default = "Metric")

	NAME_VISIBILITY = (
		('VFN', 'First name'),
		('VLN', 'Last name'),
	)
	user_first_lastname_visibility = models.CharField(max_length=3, choices = NAME_VISIBILITY, 
		null = True, default = "VFN")

	objects = MyUserManager()
	
	# username and email must always be unique
	class Meta:
		unique_together = (("email"),)
