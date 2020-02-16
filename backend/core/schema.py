"""
    Defines GraphQL Schema for core module
"""
import graphene
import graphql
from .mics import send_email
from graphene_django import DjangoObjectType
from graphql.execution.base import ResolveInfo

from core.models import Apartment, House, Room, myUser, ContactUs


class HouseType(DjangoObjectType):
    class Meta:
        model = House


class ApartmentType(DjangoObjectType):
    class Meta:
        model = Apartment


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class UserType(DjangoObjectType):
    class Meta:
        model = myUser


class ContactType(DjangoObjectType):
    class Meta:
        model = ContactUs


class Query(object):
    """ GraphQL for getting DB models

    Functions are resolvers which connect queries in the schema to actions done by the database.

    ! variable names must be same for the resolve ..functions.
    Otherwise GraphQL is not going to work.!

        .. _URL: https://stackabuse.com/building-a-graphql-api-with-django/
    """

    home_properties = graphene.List(HouseType)
    home_property = graphene.Field(HouseType, id=graphene.Int())
    room_properties = graphene.List(RoomType)
    room_property = graphene.Field(RoomType, id=graphene.Int())
    apartment_properties = graphene.List(ApartmentType)
    apartment_property = graphene.Field(ApartmentType, id=graphene.Int())
    melive_users = graphene.List(UserType)
    melive_user = graphene.Field(UserType, id=graphene.Int())

    def resolve_home_properties(self, info, **kwargs):
        return House.objects.selected_related("myUser").all()

    def resolve_apartment_properties(self, info, **kwargs):
        return Apartment.objects.selected_related("myUser").all()

    def resolve_room_properties(self, info, **kwargs):
        return Room.objects.selected_related("myUser").all()

    def resolve_melive_users(self, info, **kwargs):
        return myUser.objects.all()

    def resolve_melive_user(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return myUser.objects.get(pk=id)

        return None

    def resolve_house_property(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return House.objects.get(pk=id)

        return None

    def resolve_room_property(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Room.objects.get(pk=id)

        return None

    def resolve_apartment_property(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Apartment.objects.get(pk=id)

        return None


class ContactUs(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        subject = graphene.String(required=True)
        choices = graphene.String(required=True)
        text = graphene.String(required=True)

    contact = graphene.Field(ContactType)

    def mutate(self, info, name, email, subject, choices, text):
        send_email(info.context, userPresent_username=name, userPresent_email=email,
            subject=subject, text_msg=text)

        result = True
        return ContactUs(inputName=contactInfo.name, inputEmail=contactInfo.email, inputChoices=contactInfo.choices, inputSubject=contactInfo.subject, inputText=contactInfo.text, result=result)


class Mutation(object):
    send_contact_msg = ContactUs.Field()
