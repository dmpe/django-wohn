from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class ApartmentType(models.Model):
	"""
	Define each apartment, 1-to-n with Users
	"""
	apartment_offered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	apartment_rooms = models.IntegerField()
	apartment_created = models.DateTimeField(auto_now_add=True)
	# https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=13.04.2018
	apartment_price_eur = models.PositiveSmallIntegerField() # 0 to 32767
	apartment_price_czk = models.PositiveIntegerField() # 0 to 2147483647

class ExchangeRates(models.Model):
	"""
	parse_forex_data in misc.py
	Q: are we going to calculate forex dynamically via JS or we need to
	store all there pairs. Does user have the capability to put 
	different number ?
	"""
	OneEurCzk = models.DecimalField(max_digits=3, decimal_places=3)
	OneEurUsd = models.DecimalField(max_digits=3, decimal_places=3)
	OneUsdCzk = models.DecimalField(max_digits=3, decimal_places=3)

