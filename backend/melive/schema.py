import graphene

import core.schema
# import userMng.schema


class Mutations(graphene.ObjectType):
    """
    For POST, UPDATE, INSERT requests
    """
    pass


class Query(core.schema.Query,
            graphene.ObjectType):
    """
    For GET requests for melive.xyz
    backend.userMng.schema.Query,

    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
