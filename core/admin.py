from django.contrib import admin
from .models import *

class ApartmentTypeAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	pass

class ExchangeRateAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	template_list = "admin/currency_exchange_list.html"

	# the change list page will include a date-based 
	# drilldown navigation by that field
	date_hierarchy = 'ExchangeRate__today'
	
	# only these fields are display, i.e. all
	list_display = ['today', 
					'OneEurCzk', 
					'OneEurUsd', 
					'OneUsdCzk']

	# how many items appear on each paginated admin change list page
	list_per_page = 5

	def get_forex_data(self, request):
		dt = super(ExchangeRateAdmin, self).changelist_view(request, extra_context)

		try:
            # fetches "table" data 
			qs = dt.context_data['cl'].queryset
		except (AttributeError, KeyError):
			return dt
        
		currency_data = qs.annotate(
			period=Trunc(
				'today',
				output_field=DateTimeField(),
			),
		).values('period').filter('').order_by('period')

		# needs to have JSON object with 3 large arrays - one for each currency
        # the same then applies to the data
		dt.context_data['currency_data'] = [{
			'name': x['']
			'data': x['data']
		} for x in currency_data]

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
