from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import *

# Create your models here.
class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
	"""
	Define what users can do/have:

	user_created = uses timestamp (mutually exclusive with default=timezone.now())
	user_name = short name
	"""
	user_id = models.AutoField(primary_key=True)
	user_first_name = models.CharField(max_length = 200)
	user_last_name = models.CharField(max_length = 200)
	user_int_tel = PhoneNumberField(default=models.NOT_PROVIDED, blank=True)
	objects = MyUserManager()
    
	def __str__(self):
		return '{} ({})'.format(get_username(),  get_email_field_name())