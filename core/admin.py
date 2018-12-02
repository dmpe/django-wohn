from django.contrib import admin
from django.db.models import *
from django.db.models.functions import *

from datetime import *

from .models import *

import pandas as pd
import json
from django.core import serializers
from django.core.serializers.json import *

class ApartmentTypeAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

class UserMessageAdmin(admin.ModelAdmin):
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
		JSONdata = []
		# do not change the ordering, otherwise in change_list.html too
		for i in ['OneEurCzk', 'OneEurUsd', 'OneUsdCzk']:
			JSONdata.append(self.prepare_data(qs, i))

		# print("JSONDATA -> ", JSONdata)
		response.context_data['currency_data'] = JSONdata

		return response

	def prepare_data(self, queryset=None, currency=None):
		# select only two columns, date + currency
		two_col = queryset.values("today", currency)

		# convert to pandas, sorting epoch value min->max inplace (!)
		two_col_df = pd.DataFrame.from_records(two_col, columns = ['today', currency])
		two_col_df.sort_values(by = 'today', ascending=True, inplace=True)
		# print('we are in prepare_data func: df ->', two_col_df)
		
		# export to json object (raw data, no columns, etc.)
		prossed_data = two_col_df.to_json(orient='values')
		# print('we are in prepare_data func: prop ->', prossed_data)

		return prossed_data

admin.site.register(ApartmentType, ApartmentTypeAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
admin.site.register(UserMessage, UserMessageAdmin)