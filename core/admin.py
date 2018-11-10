from django.contrib import admin

from datetime import *
from django.db.models import *
from django.db.models.functions import *

from .models import *

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
	#date_hierarchy = 'ExchangeRate__today'
	
	# only these fields are display, i.e. all
	list_display = ['today', 
					'OneEurCzk', 
					'OneEurUsd', 
					'OneUsdCzk']

	# how many items appear on each paginated admin change list page
	list_per_page = 5

	def prepare_data(queryset=None, currency=None):
		# select only two columns, date + currency
		two_col = queryset.values("today", currency)
		# convert to pandas
		two_col_df = pd.DataFrame.from_records(two_col)
		# export to json object - to try...
		prossed_data = two_col_df.to_json()
		print(prossed_data)

		return prossed_data

	def get_forex_data(self, request):
		dt = super(ExchangeRateAdmin, self).changelist_view(request)

		try:
            # fetches "table" data 
			qs = dt.context_data['cl'].queryset
		except (AttributeErtodayror, KeyError):
			return dt
        
		# needs to have JSON object with 3 large arrays - one for each currency
        # the same then applies to the data
        # convert time to epoch
		dt.context_data['currency_data'] = prepare_data(qs, "OneEurCzk")
		dt.context_data['currency_data'] += prepare_data(qs, "OneEurUsd")
		dt.context_data['currency_data'] += prepare_data(qs, "OneUsdCzk")

		return dt

	def changelist_view(self, request, extra_context=None):
		
		extra_context = extra_context or {}
		extra_context['currency_data'] = self.get_forex_data(request)

		response = super().changelist_view(
			request,
			extra_context=extra_context,
		)

		return response

admin.site.register(ApartmentType, ApartmentTypeAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
