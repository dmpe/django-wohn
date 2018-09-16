from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	"""
	Define what users can do/have:

	user_created = uses timestamp (mutually exclusive with default=timezone.now())
	user_name = short name
	"""
	user_id = models.AutoField(primary_key=True)
	user_created = models.DateTimeField(auto_now_add=True)
	user_name = models.CharField(max_length = 30)
	user_first_name = models.CharField(max_length = 200)
	user_last_name = models.CharField(max_length = 200)
	user_email = models.EmailField()
	user_int_tel = PhoneNumberField(default=models.NOT_PROVIDED, blank=True)

	def __str__(self):
		return '{} ({})'.format(self.user_name, self.user_email)
	
	def is_authenticated(self):
		return TRUE

	def	is_active(self):
		return TRUE