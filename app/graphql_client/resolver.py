import strawberry

from service import skills
from graphql_client.models import EdgeType, GraphType, ModuleType


@strawberry.type
class Query:
    @strawberry.field
    async def graph(self, course: str = "python") -> GraphType:
        graph = await skills.get_graph_by_topic(course)
        return GraphType(
            nodes=[ModuleType(id=n.id_, label=n.label) for n in graph.nodes],
            edges=[EdgeType(**e.model_dump(by_alias=True)) for e in graph.edges],
        )

    @strawberry.field
    async def module(self, code: str) -> ModuleType:
        module = await skills.get_skill(code)
        return ModuleType(id=module.id, label=module.name)

    @strawberry.field
    async def next_module(self, code: str) -> list[ModuleType]:
        module = await skills.get_next_modules(code)
        return [ModuleType(id=m.id, label=m.name) for m in module.path]
