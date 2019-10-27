import hashlib

# for gravatar URLs and user's profile image and its unique name
import urllib

import django

# for time related tasks, incl. timezone
import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.safestring import *
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField, TimeZoneFormField

from .mics import upload_profile_image


class AbstractProperty(django.db.models.Model):
    """ Home Property (e.g. apartment, house, room)

    Define each apartment, 1-to-n with Users
    unit conversion --> https://pint.readthedocs.io/en/latest/
    """

    # will not display
    property_created = models.DateTimeField(auto_now_add=True)

    property_offered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    # Characteristics for each house and apartment
    property_rooms = models.IntegerField()
    # do not delete because part of US/Metric if else switch
    property_size_in_sq_meters = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    property_size_in_sq_foot = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    # used for calculated prices, same principle
    property_price_in_eur = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    property_price_in_czk = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    property_price_in_usd = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "properties"
        abstract = True

    def calculate_eur_czk(self):
        """
        TODO
        From eur to CZK
        """
        exr_rat = ExchangeRate.objects.last()
        return exr_rat


class House(AbstractProperty):
    """
    Additional fields for a house

    """

    house_garden_size_in_sq_meters = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Houses"


class Apartment(AbstractProperty):
    """
    Additional fields for an apartment

    """

    class Meta:
        verbose_name_plural = "Apartments"


class Room(AbstractProperty):
    """
    Additional fields for renting out a single room

    """

    class Meta:
        verbose_name_plural = "Rooms"


class ExchangeRate(models.Model):
    """
    Used for storing exchange rates for EUR, CZK and USD.

    See parse_forex_data in misc.py

    Q: 1. Are we going to calculate forex dynamically via JS or we need to
    store all there pairs. -> Store in backend, fetch data via API

    Q: 2. Does user have the capability to put different number ? -> No
    """

    today = models.DateField("Today's Date", auto_now_add=True)  # will not display
    OneEurCzk = models.DecimalField("1 EUR - CZK", max_digits=7, decimal_places=3)
    OneEurUsd = models.DecimalField("1 EUR - USD", max_digits=7, decimal_places=3)
    OneUsdCzk = models.DecimalField("1 USD - CZK", max_digits=7, decimal_places=3)


class MyUserManager(UserManager):
    """
    New manager in town.
    """

    def return_profile_image(self, email):
        """
        This functions takes user_profile_image = models.ImageField and adds gravatar logic to it as well

        1 fetch "user uploaded pictire", if none then use gravatar function
        """
        pass
        # if():
        #   avatar_profile =
        # else:
        #   avatar_profile = fetch_gravatar(email=email)
        # return avatar_profile

    def fetch_gravatar(self, email, default="https://via.placeholder.com/150"):
        """
        fetching gravatar image

        https://en.gravatar.com/site/implement/images/python/
        If none is found to be associated with the email adress, then default image is used
        """
        size = 20
        gravatar_url = (
            "https://www.gravatar.com/avatar/"
            + hashlib.md5(email.lower().encode("utf-8")).hexdigest()
            + "?"
        )
        gravatar_url += urllib.parse.urlencode({"d": default, "s": str(size)})

        return gravatar_url

    def fetch_owners_properties_count(self, user_id):
        """
        Returns number of houses per owner.
        """
        property_owner = myUser.objects.filter(pk=user_id).first()
        property_count = House.objects.filter(
            property_offered_by=property_owner
        ).count()
        print(property_count)

        return property_count


class myUser(AbstractUser):
    """
    Melive.xyz's specific user.

    Define attributes for our user class
    """

    # email, username, first and last name are unnecessary
    GENDER_CHOICES = (
        ("M", "Mr."),
        ("F", "Mrs. or Miss"),
        ("O", "Other or prefer not to say"),
    )
    user_gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, default="O"
    )
    user_int_tel = PhoneNumberField(blank=True, null=True)
    user_timezone = TimeZoneField(default=settings.TIME_ZONE)
    user_country = CountryField(default="CZ")

    # using a function here
    user_profile_image = models.ImageField(
        upload_to=upload_profile_image, blank=True, null=True
    )

    UNITS_SYSTEM = (("Imperial", "Imperial"), ("Metric", "Metric"))
    user_units_system = models.CharField(
        max_length=10, choices=UNITS_SYSTEM, null=True, default="Metric"
    )

    NAME_VISIBILITY = (("VFN", "First name"), ("VLN", "Last name"))
    user_first_lastname_visibility = models.CharField(
        max_length=3, choices=NAME_VISIBILITY, null=True, default="VFN"
    )

    objects = MyUserManager()

    # username (by default) and email must always be unique
    class Meta:
        unique_together = (("email"),)
