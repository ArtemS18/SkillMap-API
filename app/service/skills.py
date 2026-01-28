from redis_client.cache import cache_query
from schemas.skill_schema import ModuleOut, ModulePath
from schemas.graph_schema import GraphGet
from neo4j_client import client

from service import roadmap


@cache_query(time_limit=60 * 3, caching=False)  # 3 MINUTE
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
    graph = await client.get_graph(cypq, {"topic_code": topic})
    print(graph)
    return graph


@cache_query()
async def get_next_modules(id: str) -> ModulePath:
    cypq = (
        "MATCH (prev:Module)-[:REQUIRES]->(next:Module) "
        "WHERE prev.code = $id "
        "OPTIONAL MATCH (next)-[:INCLUDE]->(skill:Skill) "
        "RETURN next, collect(DISTINCT skill) AS skills "
        "ORDER BY next.code;"
    )
    path = await client.get_path(cypq, {"id": id})
    return path


async def get_path_beetwen_modules(from_id: str, to_id: str) -> ModulePath:
    return await roadmap.get_roadmap([from_id], [to_id])


@cache_query()
async def get_skill(id: str) -> ModuleOut:
    cypq = (
        "MATCH (m:Module)"
        "WHERE m.code = $id "
        "OPTIONAL MATCH (m)-[:INCLUDE]->(skill:Skill) "
        "RETURN m, collect(DISTINCT skill) AS skills "
        "ORDER BY m.code;"
    )
    skill = await client.get_skill(cypq, {"id": id})
    return skill


@cache_query(caching=False)
async def get_node_graph(node_ids: list[str]) -> GraphGet:
    print(node_ids)
    cypq = (
        "MATCH (m:Module)"
        "WHERE m.code IN $ids "
        "OPTIONAL MATCH (m)-[r]->(other:Module) "
        "WHERE other.code IN $ids "
        "RETURN collect(DISTINCT m) AS modules, collect(r) AS nextRelations;"
    )
    skill = await client.get_graph(cypq, {"ids": node_ids})
    return skill
