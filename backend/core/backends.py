from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import *
from django.core.validators import validate_email
from django.db import *

from .mics import *
from .models import myUser


class EmailUserNameAuthBackend(ModelBackend):
    """
    This is used for authentication of myUsers
    using either username or email in the input field.
    By default, username/password is used and this
    extends the approach with the email/password.

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

    def check_for_user_existence(self, inputString=None):
        """
        check in the database if the username or email does exist
        if yes, return positive bool value

        Used for email-based password reset

        :param inputString: either it can be a username or email

        :returns: user object if user found and bool value (TRUE, FALSE)
        """
        getUserObject, presentInSystem = None, False
        is_valid = validate_email(inputString)

        if is_valid is True:
            # if the input was email
            try:
                user_exists_id = myUser.objects.filter(email=inputString).first().pk
                getUserObject = myUser.objects.get(id=user_exists_id)
                presentInSystem = True
            except BaseException:
                pass
        else:
            try:
                user_exists_id = myUser.objects.filter(username=inputString).first().pk
                getUserObject = myUser.objects.get(id=user_exists_id)
                presentInSystem = True
            except BaseException:
                pass

        return [presentInSystem, getUserObject]
