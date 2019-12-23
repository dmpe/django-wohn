"""
    Overall GraphQL Schema which references those in separate modules
"""

import graphene
import core.schema


class Mutations(graphene.ObjectType):
    """
    For POST, UPDATE, INSERT requests
    """

    pass


class Query(core.schema.Query, graphene.ObjectType):
    """
    For GET requests for melive.xyz
    """

    pass


schema = graphene.Schema(query=Query)
