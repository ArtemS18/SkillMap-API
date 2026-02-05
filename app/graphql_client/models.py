import strawberry


@strawberry.type
class ModuleType:
    id: str
    label: str


@strawberry.type
class EdgeType:
    id: str
    kind: str
    source: str
    target: str


@strawberry.type
class GraphType:
    nodes: list[ModuleType]
    edges: list[EdgeType]
