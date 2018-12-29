from django.db import *
from django.db import models
from django.contrib.auth.models import *
from django.conf import *
from django_countries.fields import *

from core.models import *
# for storing user's timezone, default is Prague (CET) stored in settings.py
import pytz
from timezone_field import TimeZoneField

# store users phone number
from phonenumber_field.modelfields import PhoneNumberField

class MyUserManager(UserManager):

    def fetch_gravatar(email, default = "https://www.ienglishstatus.com/wp-content/uploads/2018/04/Anonymous-Whatsapp-profile-picture.jpg"):
	"""
	fetching gravatar image
	https://en.gravatar.com/site/implement/images/python/
	If none is found to be associated with the email adress, then default image is used
	"""
		size = 20
		gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?"
		gravatar_url += urllib.parse.urlencode({'d':default, 's':str(size)})

		return gravatar_url

	def fetch_number_of_properties_per_author(self, user_id):
		property_owner = myUser.objects.get(id=user_id)
		property_count = Property.objects.filter(property_offered_by = property_owner).count()
		
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
	
	user_profile_image = models.ImageField(upload_to = "user_profile_photos")
	
	UNITS_SYSTEM = (
		('Imperial', 'Imperial'),
		('Metric', 'Metric'),
	)
	user_units_system = models.CharField(max_length=10, choices = UNITS_SYSTEM, null = True, default = "Metric")

	NAME_VISIBILITY = (
		('VFN', 'First name'),
		('VLN', 'Last name'),
	)
	user_first_lastname_visibility = models.CharField(max_length=3, choices = NAME_VISIBILITY, null = True, default = "VFN")

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