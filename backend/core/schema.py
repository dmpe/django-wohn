"""
    Defines GraphQL Schema for core module
"""
import graphene
import graphql
from graphene_django import DjangoObjectType
from graphql.execution.base import ResolveInfo

from core.models import Apartment, House, Room, myUser


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
