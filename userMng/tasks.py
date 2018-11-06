import pickle
import time
import datetime

from __future__ import absolute_import, unicode_literals
from .mics import *
#from .celery import app

from django.utils.timezone import utc

@app.task
def add(x, y):
    return x + y

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

	# 1 EUR <> x USD
	# TODO
	ecb = Request('ECB')
	exr_flow = ecb.data(resource_id = 'EXR', 
		key={'CURRENCY': 'USD'}, 
		params = {'startPeriod': '2018'})
	daily = (s for s in exr_flow.data.series if s.key.FREQ == 'D')
	# write to pandas dataset
	cur_df = exr_flow.write(daily)
	Oneeur_usd = np.array(cur_df.iloc[[-1]]).item(0)
	
	# selected 
	exchange_dict = {
		'date': datetime.datetime.utcnow().replace(tzinfo=utc),
		'1eur_czk': Oneeur_czk,
		'1usd_czk': Oneusd_czk,
		'1eur_usd': Oneeur_usd
	}

	cur_list = [(k,v) for k,v in exchange_dict.items()]
	with open("currency_list_pickle", "wb") as fp:   #Pickling
    	pickle.dump(cur_list, fp)

	# write results to a file txt -> in production read from the file
	# with open("test.txt", "rb") as fp:   # Unpickling
		# b = pickle.load(fp)
	return exchange_dict