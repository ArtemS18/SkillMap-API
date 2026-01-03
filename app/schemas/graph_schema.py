from typing import Optional
from pydantic import BaseModel, Field
from neo4j.graph import Node, Relationship


class NodeGet(BaseModel):
    id_: str = Field(alias="id")
    kind: Optional[str] = Field(None)
    lable: str = Field(...)

    @classmethod
    def from_neo4j(cls: "NodeGet", neo_node: Node) -> "NodeGet":
        return cls(
            id=neo_node._properties.get("code"),
            kind=neo_node._properties.get("type"),
            lable=neo_node._properties.get("name"),
        )


class EdgeGet(BaseModel):
    id_: str = Field(alias="id")
    kind: str = Field(...)
    source: str = Field(...)
    target: str = Field(...)

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
