import asyncio
from redis_client.cache import cache_query
from schemas.skill_schema import ModuleOut, ModulePath, SkillOut
from schemas.graph_schema import GraphGet, NodeGet, EdgeGet
from neomodel import adb
from neo4j.graph import Node, Relationship
from neo4j_client import models

from service import roadmap


@cache_query()
async def get_graph_by_topic(topic: str) -> GraphGet:
    cypq = """
        MATCH (:Subject{code: $topic_code})-[:LEARN]->(root:Module) 
        MATCH (root)-[:REQUIRES*0..]->(m:Module) 
        WITH collect(DISTINCT m) AS all_modules
        UNWIND all_modules AS m1
        UNWIND all_modules AS m2
        MATCH (m1)-[r:REQUIRES]->(m2)
        WHERE m1 <> m2
        RETURN collect(DISTINCT all_modules) AS modules, 
       collect(DISTINCT r) AS nextRelations;
    """
    raw, _ = await adb.cypher_query(cypq, {"topic_code": topic})
    row: tuple[
        list[Node],
        list[tuple[Relationship, ...]],
    ] = raw[0]
    modules, next_rel = row
    if not modules:
        return GraphGet(nodes=[], edges=[])
    modules_nd = [NodeGet.from_neo4j(m) for m in modules[0]]
    next_edg = [EdgeGet.from_neo4j(m) for m in next_rel if m != []]

    return GraphGet(nodes=modules_nd, edges=next_edg)


@cache_query()
async def get_next_modules(id: str) -> ModulePath:
    cypq = (
        "MATCH (prev:Module)-[:REQUIRES]->(next:Module) "
        "WHERE prev.code = $id "
        "OPTIONAL MATCH (next)-[:INCLUDE]->(skill:Skill) "
        "RETURN next, collect(DISTINCT skill) AS skills "
        "ORDER BY next.code;"
    )
    raw, _ = await adb.cypher_query(cypq, {"id": id})
    roadmap = []
    for row in raw:
        m: Node = row[0]
        skills: list[Node] = row[1]
        roadmap.append(
            ModuleOut(
                id=m._properties.get("code"),
                name=m._properties.get("name"),
                skills=[
                    SkillOut(
                        id=s._properties.get("code"), name=s._properties.get("name")
                    )
                    for s in skills
                ],
            )
        )
    return ModulePath(path=roadmap)


async def get_path_beetwen_modules(from_id: str, to_id: str) -> ModulePath:
    return await roadmap.get_roadmap([from_id], [to_id])
