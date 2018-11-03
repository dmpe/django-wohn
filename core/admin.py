from django.contrib import admin
from .models import *

class ApartmentTypeAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

class ExchangeRateAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	#template_list = "index.html"
	pass

admin.site.register(ApartmentType, ApartmentTypeAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
