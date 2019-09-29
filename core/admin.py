import json
from datetime import *

import pandas as pd
from django import forms
from django.contrib import admin
from django.contrib.auth import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from django.core import serializers
from django.core.serializers.json import *
from django.db.models import *
from django.db.models.functions import *

from .models import *


class UserCreatingFormInAdmin(UserCreationForm):
    """
    By default, email is not added to the registration form
    and thus hacking is required:
    https://stackoverflow.com/a/48605586/2171456

    We extend here that user registration.
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = myUser
        fields = ("username", "password1", "password2", "email")

    def __init__(self, *args, **kwargs):
        super(UserCreatingFormInAdmin, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(UserCreatingFormInAdmin, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    add_form = UserCreatingFormInAdmin

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "user_gender",
                    "first_name",
                    "last_name",
                    "email",
                    "user_timezone",
                    "user_int_tel",
                    "user_country",
                    "user_first_lastname_visibility",
                    "user_units_system",
                    "user_profile_image",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "user_timezone",
        "user_int_tel",
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email"),
            },
        ),
    )


class PropertyAdmin(admin.ModelAdmin):
    """docstring for ClassName"""

    pass


class ExchangeRateAdmin(admin.ModelAdmin):
    """docstring for ClassName
    https://stackoverflow.com/q/39123348/2171456
    https://stackoverflow.com/a/7811582/2171456
    https://stackoverflow.com/a/14087471/2171456
    """

    template_list = "admin/currency_exchange_list.html"

    # the change list page will include a date-based
    # drilldown navigation by that field
    # todo here
    date_hierarchy = "today"

    # only these fields are display, i.e. all
    list_display = ["today", "OneEurCzk", "OneEurUsd", "OneUsdCzk"]

    # how many items appear on each paginated admin change list page
    list_per_page = 5

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            # fetches "table" data
            qs = response.context_data["cl"].queryset
        except (AttributeErtodayror, KeyError):
            return response

        # needs to have JSON object with 3 large arrays - one for each currency
        # the same then applies to the data
        JSONdata = []
        # do not change the ordering, otherwise in change_list.html too
        for i in ["OneEurCzk", "OneEurUsd", "OneUsdCzk"]:
            JSONdata.append(self.prepare_data(qs, i))

        # print("JSONDATA -> ", JSONdata)
        response.context_data["currency_data"] = JSONdata

        return response

    def prepare_data(self, queryset=None, currency=None):
        # select only two columns, date + currency
        two_col = queryset.values("today", currency)

        # convert to pandas, sorting epoch value min->max inplace (!)
        two_col_df = pd.DataFrame.from_records(two_col, columns=["today", currency])
        two_col_df.sort_values(by="today", ascending=True, inplace=True)
        # print('we are in prepare_data func: df ->', two_col_df)

        # export to json object (raw data, no columns, etc.)
        prossed_data = two_col_df.to_json(orient="values")
        # print('we are in prepare_data func: prop ->', prossed_data)

        return prossed_data


admin.site.register(myUser, UserAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
