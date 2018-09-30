from django.conf import settings
from django.contrib.auth.hashers import *
from django.contrib.auth.backends import ModelBackend
from .models import myUser
from .mics import *

class EmailUserNameAuthBackend(ModelBackend):
	"""This is used for authentication of myUsers
	using either username or email in the input field.	
	By default, username/password is used and this 
	extends this with email/password.

	Should work on /admin/ and on /administration/
	"""
	
	def get_user(self, user_id):
		try:
			return myUser.objects.get(pk=user_id)
		except myUser.DoesNotExist:
			raise None

	def authenticate(self, request, username=None, password=None):
		# username as parameter is here just as 'something'
		try:
			user = myUser.objects.get(email=username)
			if user.check_password(password):
				return user

		except myUser.DoesNotExist:
			try:
				# must always work
				user = myUser.objects.get(username=username)
				if user.check_password(password):
					return user
			except myUser.DoesNotExist:
				return None
	
	def check_for_existance(self, inputString= None):
		"""
		check in the database if the username or email does exist
		if yes, return positive bool value

		:param inputString: either it can be a username or email

		:returns: bool value if user/email is found
		"""
		#self.inputString = inputString

		# define username and email
		getUsername, getEmail, presentInSystem = None, None, False
		is_valid = valid_email(in_str = inputString)

		#print("in the checking function: is valid: " + str(is_valid))

		if is_valid is True:
			#if the input is email
			user_exists = myUser.objects.filter(email=inputString).exists()
			getEmail = inputString
			getUsername = myUser.objects.filter(email=inputString).first().get_username()
		else:
			user_exists = myUser.objects.filter(username=inputString).exists()
			getEmail = myUser.objects.filter(username=inputString).first().email
			getUsername = inputString

		if user_exists is True:
			presentInSystem = True
		else:
			presentInSystem = False

		#print("in the checking function: return value is " + str(presentInSystem))
		
		return [presentInSystem, getUsername, getEmail]