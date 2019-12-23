# for rendering markdown files
# instance of a logger
import logging

from django import forms
from django.conf import settings
from django.contrib import *
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import *
from django.contrib.auth.mixins import *
from django.contrib.auth.tokens import *
from django.core.exceptions import *
from django.core.mail import *
from django.db import *
from django.http import *
from django.shortcuts import *
from django.template import *
from django.template.loader import render_to_string
from django.urls import *
from django.utils.encoding import *
from django.utils.html import *
from django.utils.http import *
from django.utils.safestring import *
from django.views import View
from django.views.generic import *

# a generic view for creating and saving an object (e.g. user)
from django.views.generic.edit import CreateView

# for using not only username/pswd but also email/pswd
from .backends import EmailUserNameAuthBackend
from .forms import *
from .mics import *

logger = logging.getLogger(__name__)

################
#######
####### Function based views
#######
################
# Main Page/Homepage
def homepage(request):
    return render(request, "index.html")


################
#######
####### Class based views
#######
################
class ContactView(View):
    """
    Contact Form using Django approach to constructing
    forms.
    """

    template_name = "contact.html"

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["inputName"]
            email = form.cleaned_data["inputEmail"]
            subject = form.cleaned_data["inputSubject"]
            text_msg = form.cleaned_data["inputText"]

            # if is_human(recap_token) is True:
            prepare_visitor_mssg_email(request, username, email, subject, text_msg)

            messages.add_message(
                request,
                messages.SUCCESS,
                mark_safe(
                    "<h6 class="
                    "alert-heading"
                    ">Thank you for sending us the message!</h6>"
                    "<p>We wiill respond to you <strong>as soon as possible</strong>.</p>"
                ),
            )
            # else:
            #     messages.add_message(
            #         request,
            #         messages.WARNING,
            #         mark_safe(
            #             "<h6 class="
            #             "alert-heading"
            #             ">Sorry, but you seem to be a computer bot.</h6>"
            #             "<p>Please resend the message again, clean cookies or click on the right to email us directly.</p>"
            #         ),
            #     )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                mark_safe(
                    "<h6 class="
                    "alert-heading"
                    ">You message does not fulfill our basic requirenements!</h6>"
                    "<p>Check that all fields are filled correctly.</p>"
                ),
            )

        return render(request, self.template_name, {"form": form})


###################################
################
################ Passoword Reset
################
###################################
class ResetPasswordStepOneView(View):
    """
    This class takes an input from the post request and prepares & sends HTML
    email to the user
    """

    template_name = "reset_password.html"

    def post(self, request):
        """
        sends email message to the user's email address
        """
        inputEmail_Username = request.POST.get("inputEmail_Username", False)
        token_obj = PasswordResetTokenGenerator()

        # check if user is present in the database -> moved to backend
        userPresent = EmailUserNameAuthBackend.check_for_user_existence(self, inputEmail_Username)

        if userPresent[0] is True:
            tk = token_obj.make_token(userPresent[1])
            uid = urlsafe_base64_encode(force_bytes(userPresent[1].pk))

            prepare_psswd_reset_email(
                request,
                userPresent_username=userPresent[1].get_username(),
                userPresent_email=userPresent[1].email,
                userPresent_token=tk,
                userPresent_uid=uid,
            )

            messages.add_message(
                request,
                messages.SUCCESS,
                mark_safe(
                    "<h4 class="
                    "alert-heading"
                    ">Password reset was successful!</h4>"
                    "<p>Check your email now to set a new one.</p>"
                    "<p>You can now <strong>close</strong> this page.</p>"
                ),
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                mark_safe(
                    "<h4 class="
                    "alert-heading"
                    ">Password reset cannot proceed!</h4>"
                    "<p>Check your input as the user cound not be found in the database.</p>"
                    "<p>Please, try again.</p>"
                ),
            )

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ResetPasswordNewStepTwoView(View):
    """
    at this stage, a token should have been send to the user via email
    user clicks, inputs passwords, confirms and he should be able to load the main login screen
    """

    template_name = "reset_password_new.html"

    def post(self, request, *args, **kwargs):
        inputNewPassword = request.POST.get("inputNewPassword", False)
        inputConfirmNewPassword = request.POST.get("inputConfirmNewPassword", False)

        # we dont know who is the user, hence need to fetch from the URL
        myuser = validate_password_reset(request)

        if myuser is not None and inputNewPassword == inputConfirmNewPassword:
            myuser.set_password(inputNewPassword)
            myuser.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                format_html(
                    (
                        "<h4 class="
                        "alert-heading"
                        ">Your Password has been changed!</h4>"
                        '<p>You can <a href="{}" class="alert-link">now login using new credentials on the login page</a>.</p>'
                    ),
                    reverse("core:login"),
                ),
            )
        else:
            messages.add_message(
                request,
                messages.WARNING,
                mark_safe(
                    "<h4 class="
                    "alert-heading"
                    ">New passwords do not match</h4>"
                    "<p>Make sure that they are same, e.g. by checking the capital letters.</p>"
                ),
            )

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        # TODO: should actually display error and not be displayed at all
        # actually this will never be displayed unless full url
        return render(request, self.template_name)


###################################
################
################ Registration
################
###################################
class RegistrationView(CreateView):
    """docstring for RegistrationView
    """

    template_name = "signup_login/register.html"

    def post(self, request, *args, **kwargs):
        # recieve data from the registration form
        inputUsername = request.POST.get("inputUsername", False)
        inputEmail = request.POST.get("inputEmail", False)
        inputNewPassword = request.POST.get("inputNewPassword", False)
        inputConfirmNewPassword = request.POST.get("inputConfirmNewPassword", False)

        if inputNewPassword == inputConfirmNewPassword:
            try:
                ur = myUser.objects.create_user(inputUsername, inputEmail)
                ur.set_password(inputNewPassword)
                ur.is_active = True
                ur.save()
            except (IndexError, IntegrityError, ValidationError) as e:
                messages.add_message(
                    request,
                    messages.WARNING,
                    format_html(
                        (
                            "<h4 class="
                            "alert-heading"
                            ">Username or Email already exist</h4>"
                            "<p>It seems that your username and/or email already exist in our system.</p>"
                            "<p>You can reset <a class = "
                            "alert-link"
                            ' href="{}">your password</a> or provide'
                            "again a unique combination of username & email.</p>"
                        ),
                        reverse("reset_password"),
                    ),
                )

                return render(request, self.template_name)
        else:
            messages.add_message(
                request,
                messages.WARNING,
                mark_safe(
                    "<h4 class="
                    "alert-heading"
                    ">New passwords do not match</h4>"
                    "<p>Make sure that they are same, e.g. by checking the capital letters.</p>"
                ),
            )

            return render(request, self.template_name)

        auser = EmailUserNameAuthBackend.authenticate(self, request, username=inputUsername, password=inputNewPassword)

        try:
            django_login(request, auser, backend="core.backends.EmailUserNameAuthBackend")
            return redirect("userMng:userMng_index")
        except Exception as e:
            return redirect(settings.LOGIN_URL)

    def get(self, request, *args, **kwargs):
        # if get request, just render the template, with form
        return render(request, self.template_name)


###################################
################
################ Log In + Log Out
################
###################################
class LoginView(View):
    """
    Uses class based view
    """

    template_name = "signup_login/login.html"

    def post(self, request, *args, **kwargs):
        # recieve
        username_email = request.POST.get("inputEmail_Username", False)
        user_password = request.POST.get("inputNewPassword", False)

        # if is_human(recap_token):
        try:
            auth_user = EmailUserNameAuthBackend.authenticate(
                self, request, username=username_email, password=user_password
            )

            if auth_user is None:
                messages.add_message(
                    request,
                    messages.WARNING,
                    mark_safe(
                        "<h4 class="
                        "alert-heading"
                        ">Such a user does not exist.</h4>"
                        "<p>Make sure that username and password are correct.</p>"
                    ),
                )
            else:
                try:
                    # whether the user is active or not is already checked by the
                    # ModelBackend we use
                    django_login(request, auth_user, backend="core.backends.EmailUserNameAuthBackend")
                    return redirect("userMng:userMng_index")
                except Exception as e:
                    raise e

        except Exception as e:
            raise e
        # user is bot
        # else:
        #     messages.add_message(
        #         request,
        #         messages.WARNING,
        #         mark_safe(
        #             "<h4 class="
        #             "alert-heading"
        #             ">Sorry, but you seem to be a computer bot.</h4>"
        #             "<p>Please contact us if you believe you were wrongly identified because of Google Recaptha v3.</p>"
        #             "<p>Solution: clear your cookies and try again.</p>"
        #         ),
        #     )

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        # if get request just render the template, with form
        return render(request, self.template_name)


class LogoutView(View):
    """
    Class based view for logout
    Only requires get method
    """

    def get(self, request):
        django_logout(request)
        return redirect("core:homepage")
