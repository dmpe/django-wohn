from __future__ import absolute_import, unicode_literals
# because it must occur there at the beginning

# to save forex data in the python's pickle 
import pickle

# dont need because when saved, date/time is automatically added
# but still needed due to UTC and year in the request
import datetime
from django.utils.timezone import utc

# store forex data in the model
from core.models import *

# import for (forex) data processing
import pandas as pd
import numpy as np
from pandasdmx import *
from pandasdmx.api import *

# some other imports too
from .mics import *

# imports settings and our schedulling for the task
from vanoce.celery import app

# for logging the ECB connection
import logging

logger = logging.getLogger(__name__)

@app.task
def parse_forex_data(*init, **kwargs):
	"""
	A Celery task. See settings file for how it is sheduled
	Runs every month
	https://stackoverflow.com/a/38286238
	https://realpython.com/asynchronous-tasks-with-django-and-celery/
	"""
	# {EUR, USD} <> CZK
	csob_forex = "https://www.csob.cz/portal/lide/kurzovni-listek/-/date/kurzy.txt"
	data = pd.read_csv(csob_forex, delimiter = ";", skiprows=3, encoding="utf-8")
	data = data.rename({"Měna": 'currency', "Střed.1":'exchange_rate_czk'}, axis='columns')
	
	Oneeur_czk = data[data['currency'].isin(["EUR", "USD"])].iloc[0]['exchange_rate_czk']
	Oneusd_czk = data[data['currency'].isin(["EUR", "USD"])].iloc[1]['exchange_rate_czk']
	Oneeur_usd = None

	# used for ECB request and exchange_dict if necessary
	current_date = datetime.datetime.utcnow().replace(tzinfo=utc)

	# 1 EUR <> USD
	ecb = Request('ECB')

	try:
		exr_flow = ecb.data(resource_id = 'EXR', 
			key={'CURRENCY': 'USD'}, 
			params = {'startPeriod': str(current_date.year)})
		daily = (s for s in exr_flow.data.series if s.key.FREQ == 'D')

		# write to pandas dataset
		cur_df = exr_flow.write(daily)
		Oneeur_usd = np.array(cur_df.iloc[[-1]]).item(0)

	# server maintanance - e.g. error 500
	except SDMXException as e:
		print(e)
		logger.WARNING(e)
	
	if (Oneeur_usd is not None):
		# selected 
		exchange_dict = {
			#'date': current_date,
			'1eur_czk': Oneeur_czk,
			'1usd_czk': Oneusd_czk,
			'1eur_usd': Oneeur_usd
		}

		#Pickling to file system
		cur_list = [(k,v) for k,v in exchange_dict.items()]
		with open("currency_list_pickle", "wb") as fp:   
			pickle.dump(cur_list, fp)
		
		# write our data to the database model so that we can query it in the 
		# admin page and show highstock chart
		forex_model = ExchangeRate()
		forex_model.OneEurCzk = exchange_dict['1eur_czk']
		forex_model.OneUsdCzk = exchange_dict['1usd_czk']
		forex_model.OneEurUsd = exchange_dict['1eur_usd']
		forex_model.save()
		return exchange_dict
	
	else:
		print("var Oneeur_usd is empty/null because connection to the server could not have been established")
		return None

	# write results to a file txt -> in production read from the file
	# with open("test.txt", "rb") as fp:   # Unpickling
		# b = pickle.load(fp)
	