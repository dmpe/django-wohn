from django.conf import settings
from django.contrib.auth.hashers import *
from django.contrib.auth.backends import ModelBackend
from .models import myUser

class EmailUserNameAuthBackend(ModelBackend):
	"""This is used for authentication of myUsers
	using either username or email in the input field.	
	By default, username/password is used and this 
	extends this with email/password.
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
			if user.check_password(password)
				return user

		except myUser.DoesNotExist:
			try:
				# must always work
				user = myUser.objects.get(username=username)
				if user.check_password(password)
					return user
			except myUser.DoesNotExist:
				return None
				