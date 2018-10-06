######### This class is for a variety of purposes.
from werkzeug.useragents import *
from django.utils.html import *
from django.utils.http import *
from django.utils.encoding import *
from django.contrib.auth.tokens import *
from django.contrib.auth import *
import re
import requests as requests_library

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
	secret_key_recaptcha_v3 = "6LfeynMUAAAAAEv7OvF8-y1DAGfJH6vDyyjdpcTA"
	payload = {'response':recaptcha_token, 'secret':secret_key_recaptcha_v3}
	response_ggl = requests_library.post("https://www.google.com/recaptcha/api/siteverify", payload)
	response_text = json.loads(response.text)

    if response_text["score"] >= 0.5:
    	return True
    else:
    	return False
