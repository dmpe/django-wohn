from django.db import models

# Create your models here.
class ApartmentType(models.Model):
	"""
	Define each apartment, 1-to-n with Users
	"""
	#apartment_offered_by = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
	apartment_rooms = models.IntegerField()
	apartment_created = models.DateTimeField(auto_now_add=True)
	# https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=13.04.2018
	apartment_price_eur = models.PositiveSmallIntegerField()
	apartment_price_czk = models.PositiveIntegerField()
		