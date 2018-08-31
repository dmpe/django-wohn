from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
	"""
	Define what users can do/have
	"""
	user_id = models.AutoField(primary_key=True)
	user_created = models.DateTimeField(auto_now_add=True)
	user_first_name = models.CharField(max_length = 200)
	user_last_name = models.CharField(max_length = 200)
	user_email = models.EmailField()
	user_int_tel = models.PhoneNumberField(default=models.NOT_PROVIDED, null=True)

class ApartmentType(models.Model):
	"""
	Define each apartment, 1-to-n with Users
	"""
	apartment_offered_by = models.ForeignKey(User, on_delete=models.CASCADE)
	apartment_rooms = models.IntegerField()
	apartment_created = models.DateTimeField(auto_now_add=True)
	# https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=13.04.2018
	apartment_price_eur = models.PositiveSmallIntegerField()
	apartment_price_czk = models.PositiveIntegerField()
		