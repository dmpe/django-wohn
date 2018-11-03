from __future__ import absolute_import, unicode_literals
from .mics import *
from .celery import app


@app.task
def add(x, y):
    return x + y

@app.task
def parse_forex_data(*init, **kwargs):
	"""
	TODO Celery task
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
	cur_df = data_response.write(daily)
	# selected 

	exchange_dict = {
		'1eur_czk': Oneeur_czk,
		'1usd_czk': Oneusd_czk,
		'1eur_usd': '1eur_usd'
	}

	return exchange_dict