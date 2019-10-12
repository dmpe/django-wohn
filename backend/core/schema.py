import graphene
from graphene_django import DjangoObjectType
from core.models import Property, myUser


class PropertyType(DjangoObjectType):
    class Meta:
        model = Property


class UserType(DjangoObjectType):
    class Meta:
        model = myUser


class Query(object):
    all_properties = graphene.List(PropertyType)
    all_users = graphene.List(UserType)

    def resolve_all_properties(self, info, **kwargs):
        return Property.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return myUser.objects.all()
