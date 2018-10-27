######### This class is for a variety of purposes.
from werkzeug.useragents import *
from django.utils.html import *
from django.utils.http import *
from django.core.mail import *
from django.utils.encoding import *
from django.contrib.auth.tokens import *
from django.contrib.auth import *
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import *
# for messages
from django.utils.safestring import *
import re
import json
import requests as requests_library
import pandas as pd

#for forex data
from pandasdmx import *

# replaced by logic in contrib.auth.tokens
def http_headers(request):
	""" extracts HTTP headers from client's request
	"""
	ua = UserAgent(request.META['HTTP_USER_AGENT'])
	ip = request.META['REMOTE_ADDR']

	operating_system = ua.platform
	ip_address = ip
	browser = ua.browser
	browser_version = ua.version

	return [operating_system, ip_address, browser, browser_version]

def valid_email(in_str = None):
	""" 
	validating emails are mess
	applies idea that it must have @ and >=1 . after @
	https://stackoverflow.com/a/8022584
	"""
	email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
	email_valid = False

	if not email_regex.match(in_str):
		email_valid = False
	else:
		email_valid = True

	return email_valid

def get_uid_token(request):
	"""
	string that one gets is 
	/new_password/NQ/504-56db758854211636d9fc/
	regex for token = re.compile(r'(/.*/(.*)/)')
	regex for uid part: (/.*/(.*)/(.*)/)
	"""
	current_url = request.get_full_path()
	uid = current_url.split("/")[2]
	token = current_url.split("/")[3]

	return [uid, token]

def validate_password_reset(request):
	"""
	Take current URL and check whether token matches what one expects
	Borrowed from https://github.com/mhacks/mhacks-admin/blob/master/MHacks/utils.py#L143
	"""
	my_user_model = get_user_model()
	tkn = PasswordResetTokenGenerator()
	uid, token = get_uid_token(request)

	users_pk = urlsafe_base64_decode(uid).decode()
	us = my_user_model.objects.get(pk=users_pk)

	if us is not None and tkn.check_token(us, token):
		return us
	else:
		print("token is not valid")
		return None

def is_human(recaptcha_token = None):
	"""
	Used for token verification. 
	Borrowed from https://techmonger.github.io/5/python-flask-recaptcha/
	"""
	payload = {'response':recaptcha_token, 'secret':settings.GOOGLE_RECAPTCHA_V3}
	response_ggl = requests_library.post("https://www.google.com/recaptcha/api/siteverify", payload)
	response_text = json.loads(response_ggl.text)
	print(response_text)

	if response_text["success"] is True and response_text["score"] >= 0.3:
		return True
	else:
		return False

def prepare_psswd_reset_email(request, userPresent_username = None, 
	userPresent_email = None, userPresent_token = None, userPresent_uid = None):

	subject = 'B40.cz: Password Reset'
	smtp_email = settings.DEFAULT_FROM_EMAIL

	client_headers = http_headers(request)

	cntxt = {"username": userPresent_username, "token": userPresent_token, 
		"password_expire": settings.PASSWORD_RESET_TIMEOUT_DAYS, "uid": userPresent_uid,
		"operating_system": client_headers[0], "ip_address": client_headers[1], 
		"browser": client_headers[2], "browser_version": client_headers[3]}

	html_message = render_to_string('reset_password_email.html', cntxt)
	plain_message = strip_tags(html_message)

	try:
		send_mail(subject, plain_message, smtp_email, [userPresent_email], html_message=html_message)
	except BadHeaderError:
		return HttpResponse('Invalid header found.')

	return None

def prepare_visitor_mssg_email(request, userPresent_username = None, 
	userPresent_email = None, subject = None, text_msg = None):

	subject = 'B40.cz: Message from the user/visitor: ' + subject
	smtp_email = settings.DEFAULT_FROM_EMAIL
	my_email = settings.MY_EMAIL
	from_email = userPresent_email

	client_headers = http_headers(request)

	cntxt = {"username": userPresent_username, "from_email" : from_email, "text_msg": text_msg,
		"operating_system": client_headers[0], "ip_address": client_headers[1], 
		"browser": client_headers[2], "browser_version": client_headers[3]}

	html_message = render_to_string("new_visitor_email.html", cntxt)
	plain_message = strip_tags(html_message)

	try:
		send_mail(subject, plain_message, smtp_email, [my_email], html_message=html_message)
	except BadHeaderError:
		return HttpResponse('Invalid header found.')

	return None

def parse_forex_data(*init, **kwargs):
	"""
	TODO Celery task
	https://stackoverflow.com/a/38286238
	https://realpython.com/asynchronous-tasks-with-django-and-celery/
	"""
	# {EUR, USD} <> CZK
	csob_forex = "https://www.csob.cz/portal/lide/kurzovni-listek/-/date/kurzy.txt"
	data = pd.read_csv(csob_forex, delimiter = ";", skiprows=3, encoding="utf-8")
	data = data.rename({"Měna": 'currency', "Střed.1":'exchange_rate_czk'}, axis='columns').
	
	1eur_czk = data[data['currency'].isin(["EUR", "USD"])].iloc[0]['exchange_rate_czk']
	1usd_czk = data[data['currency'].isin(["EUR", "USD"])].iloc[1]['exchange_rate_czk']

	# 1 EUR <> x USD
	ecb = Request('ECB')
	exr_flow = ecb.data(resource_id = 'EXR', 
		key={'CURRENCY': 'USD'}, 
		params = {'startPeriod': '2018'})
	daily = (s for s in exr_flow.data.series if s.key.FREQ == 'D')
	cur_df = data_response.write(daily)
	# selected 

	exchange_dict = {
		'1eur_czk': 1eur_czk
		'1usd_czk': 1usd_czk
		'1eur_usd': 1eur_usd
	}
	return exchange_dict