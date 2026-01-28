from typing import Optional
from pydantic import BaseModel, Field
from neo4j.graph import Node, Relationship


class NodeMetaData(BaseModel):
    category: Optional[str] = Field(None)


class NodeGet(BaseModel):
    id_: str = Field(alias="id")
    data: NodeMetaData = Field(...)
    label: str = Field(...)

    class Config:
        populate_by_name = True
        from_attributes = True

    @classmethod
    def from_neo4j(cls: "NodeGet", neo_node: Node) -> "NodeGet":
        categories = list(filter(lambda x: x != "Module", list(neo_node.labels)))
        return cls(
            id=neo_node._properties.get("code"),
            data=NodeMetaData(category=None if len(categories) < 1 else categories[0]),
            label=neo_node._properties.get("name"),
        )


class EdgeGet(BaseModel):
    id_: str = Field(alias="id")
    kind: str = Field(...)
    source: str = Field(...)
    target: str = Field(...)

    class Config:
        populate_by_name = True
        from_attributes = True

    @classmethod
    def from_neo4j(cls: "EdgeGet", neo_edg: Relationship) -> "EdgeGet":
        return cls(
            id=neo_edg.element_id,
            kind=neo_edg.type,
            source=neo_edg.nodes[0]._properties.get("code"),
            target=neo_edg.nodes[1]._properties.get("code"),
        )


class GraphGet(BaseModel):
    nodes: list[NodeGet]
    edges: list[EdgeGet]
