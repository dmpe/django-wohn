from django.contrib import admin
from .models import *

class ApartmentTypeAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

class ExchangeRatesAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

admin.site.register(ApartmentType, ApartmentTypeAdmin)
admin.site.register(ExchangeRates, ExchangeRatesAdmin)
