from django.contrib import admin
from django.db.models import *
from django.db.models.functions import *

from datetime import *

from .models import *

import pandas as pd

class ApartmentTypeAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

class ExchangeRateAdmin(admin.ModelAdmin):
	"""docstring for ClassName
	https://stackoverflow.com/q/39123348/2171456
	https://stackoverflow.com/a/7811582/2171456
	https://stackoverflow.com/a/14087471/2171456
	"""
	template_list = "admin/currency_exchange_list.html"

	# the change list page will include a date-based 
	# drilldown navigation by that field
	# todo here
	date_hierarchy = 'today'
	
	# only these fields are display, i.e. all
	list_display = ['today', 
					'OneEurCzk', 
					'OneEurUsd', 
					'OneUsdCzk']

	# how many items appear on each paginated admin change list page
	list_per_page = 5

	def changelist_view(self, request, extra_context=None):
		response = super().changelist_view(
			request,
			extra_context=extra_context,
		)

		try:
            # fetches "table" data 
			qs = response.context_data['cl'].queryset
		except (AttributeErtodayror, KeyError):
			return response
        
		# needs to have JSON object with 3 large arrays - one for each currency
        # the same then applies to the data
        # convert time to epoch
		response.context_data['currency_data'] = self.prepare_data(qs, "OneEurCzk")
		# response.context_data['currency_data'] += self.prepare_data(qs, "OneEurUsd")
		# response.context_data['currency_data'] += self.prepare_data(qs, "OneUsdCzk")

		print(response.context_data['currency_data'])
		
		return response
# {"OneEurCzk":{"0":26.358},"today":{"0":1541203200000}}
# {"OneEurUsd":{"0":1.147},"today":{"0":1541203200000}}
# {"OneUsdCzk":{"0":19.22},"today":{"0":1541203200000}}

	def prepare_data(self, queryset=None, currency=None):
		# select only two columns, date + currency
		two_col = queryset.values_list("today", currency)
		# convert to pandas
		two_col_df = pd.DataFrame.from_records(two_col, columns = ['today', currency])
		# export to json object - to try...
		prossed_data = two_col_df.to_json()
		print(prossed_data)

		return prossed_data

admin.site.register(ApartmentType, ApartmentTypeAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
