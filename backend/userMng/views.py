from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import *
from django.contrib.auth.mixins import *
from django.contrib.auth.tokens import *
from django.core.exceptions import *
from django.core.mail import send_mail
from django.db import *
from django.http import *
from django.shortcuts import *
from django.template import *
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import *
from django.utils.html import *
from django.utils.http import *
from django.utils.safestring import *
from django.views import View
# a generic view for creating and saving an object (e.g. user)
from django.views.generic.edit import CreateView

from userMng.third_party_services.google_analytics import *

from .forms import *

################
#######
####### Function based views
#######
################

################
#######
####### Class based views
#######
################

###########################################
#######
####### User Profile Administration / Listing of properties
#######
###########################################
class UserProfileIndex(LoginRequiredMixin, View):
    """
    The homepage of the administration - the essential Dashboard for the User
    Used for displaying information and submitting new feature requests
    """

    template_name = "user_adm_index.html"

    def post(self, request):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.cleaned_data["inputFeedback"]

            prepare_visitor_mssg_email(
                request,
                userPresent_username=request.user.get_username(),
                userPresent_email=request.user.email,
                subject="User's Feedback: ",
                text_msg=feedback,
            )

            messages.add_message(
                request,
                messages.SUCCESS,
                mark_safe(
                    "<h6 class="
                    "alert-heading"
                    ">Thank you for sending us the message!</h6>"
                    "<p>We will respond to you <strong>as soon as possible</strong>.</p>"
                ),
            )
        else:
            # form must contain some text !
            messages.add_message(
                request,
                messages.ERROR,
                mark_safe(
                    "<h6 class="
                    "alert-heading"
                    ">You message does not fulfill our basic requirements!</h6>"
                    "<p>Check that all fields are filled correctly.</p>"
                ),
            )

        return render(request, self.template_name, {"form": form})

    def get(self, request):
        """docstring for get
        """
        form = FeedbackForm()

        gh = Google_Analytics()
        keyDrop = gh.getAzureSecret()
        gh.download_file(keyDrop)
        analytics = gh.initialize_analyticsreporting()
        response = gh.get_report(analytics)
        number_of_views = gh.print_response(response)

        number_of_user_properties = myUser.objects.fetch_owners_properties_count(
            user_id=request.user.pk
        )

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "number_of_views": number_of_views.get("ga:pageviews"),
                "number_of_properties": number_of_user_properties,
            },
        )


class UserProfileAdministration(LoginRequiredMixin, View):
    """
    The homepage for user profile - where the settings can be changed
    """

    template_name = "user_profile.html"

    def post(self, request):
        """call UserProfileForm
        """
        form = UserProfileForm(request.POST)

        if form.is_valid():
            myUser.objects.filter(pk=request.user.pk).update(**request.data)
            myUser.save()

        return render(request, self.template_name, {"form": form})

    def get(self, request):
        """
        by default the image is something from gravatar
        """
        form = UserProfileForm()
        gravatar_url = myUser.objects.fetch_gravatar(email=request.user.email)
        number_of_user_properties = myUser.objects.fetch_owners_properties_count(
            user_id=request.user.pk
        )

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "gravatar_url": gravatar_url,
                "number_of_properties": number_of_user_properties,
            },
        )


class UserProfileProperties(LoginRequiredMixin, View):
    """
    The homepage for user's properties - their list and small dashboard
    """

    template_name = "user_property.html"

    def post(self, request):
        """
        docstring for post
        """
        pass

    def get(self, request):
        """
        docstring for get
        """
        form = NewPropertyForm()
        number_of_user_properties = myUser.objects.fetch_owners_properties_count(
            user_id=request.user.pk
        )
        return render(
            request,
            self.template_name,
            {"form": form, "number_of_properties": number_of_user_properties},
        )


###################################
################
################ For advertising purpose
################
###################################
class AdvertisingMyAdd(LoginRequiredMixin, View):
    """docstring for UserAds
    """

    template_name = "ads/my_ads.html"

    def get(self, request):
        return render(request, self.template_name)

    def post():
        pass


class AdvertisingStatistics(LoginRequiredMixin, View):
    """docstring for AdvertisingStatistics
    """

    template_name = "ads/statistics.html"

    def get(self, request):
        return render(request, self.template_name)

    def post():
        pass
