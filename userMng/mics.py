######### This class is for a variety of purposes.
from werkzeug.useragents import *
import re

# replaced by logic in contrib.auth.tokens
def gen_password_reset_token():
	pass

def http_headers(self, request):
	""" extracts HTTP headers from client's request

	"""
	self.request = request
	ua = UserAgent(request.META['HTTP_USER_AGENT'])
	ip = request.META['REMOTE_ADDR']

	operating_system = ua.platform
	ip_address = ip
	browser = ua.browser
	browser_version = ua.version

	return [operating_system, ip_address, browser, browser_version]

def valid_email(self, in_str = None):
	""" validating emails are mess
	applies idea that it must have @ and >=1 . after @
	https://stackoverflow.com/a/8022584
	"""
	self.in_str = in_str
	email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
	
	email_valid = False

	if not email_regex.match(in_str):
		email_valid = False
	else:
		email_valid = True

	return email_valid