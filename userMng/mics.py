######### This class is for a variety of purposes.
from werkzeug.useragents import *
from django.utils.html import *
from django.utils.http import *
from django.utils.encoding import *
from django.contrib.auth.tokens import *

import re

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
	""" validating emails are mess
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
	current_url = request.get_full_path()

	print(current_url)

	return "test"
	#[uid, token]



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
		return user
	else:
		print("token is not valid")
		return None

