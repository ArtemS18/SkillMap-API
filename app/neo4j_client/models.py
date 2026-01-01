from neomodel import (UniqueIdProperty, get_config, AsyncStructuredNode, StringProperty, AsyncRelationshipTo)


config = get_config()
config.database_url = 'bolt://neo4j:password@localhost:7687'

class Skill(AsyncStructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    
    type = StringProperty()


class Module(AsyncStructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    type = StringProperty()

    next = AsyncRelationshipTo("Module", 'NEXT')
    skills = AsyncRelationshipTo("Skill", 'INCLUDE')

