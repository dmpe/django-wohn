from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Property(models.Model):
	"""
	Define each apartment, 1-to-n with Users
	unit conversion --> https://pint.readthedocs.io/en/latest/
	"""
	property_created = models.DateTimeField(auto_now_add=True) # will not display

	property_offered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	# Characteristics for each house and apartment
	property_rooms = models.IntegerField()
	# calculate square foot on the fly, via pint
	property_size_in_sq_meters = models.DecimalField(max_digits=7, decimal_places=2) 
	# used for calculated prices, same principle
	property_price_in_eur = models.DecimalField(max_digits=7, decimal_places=2) 
	property_price_in_czk = models.DecimalField(max_digits=7, decimal_places=2) 
	property_price_in_usd = models.DecimalField(max_digits=7, decimal_places=2) 

	class Meta:
		verbose_name_plural = "properties"

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
	
class UserMessage(models.Model):
	"""
	For private communication.
	https://stackoverflow.com/questions/35310283/how-to-model-messages-exchanged-between-users-er-diagram
	"""
	send_date = models.TimeField(auto_now_add=True) # will not display
	from_whom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="from_whom_user", on_delete=models.CASCADE)
	to_whom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="to_whom_user", on_delete=models.CASCADE)
	inputMessage = models.TextField()