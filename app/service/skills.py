from logging import getLogger
from redis_client.cache import cache_query
from pydantic_schemas.skill_schema import Link, ModuleDetails, ModuleOut, ModulePath
from pydantic_schemas.graph_schema import GraphGet
from neo4j_client import client
from db import models

from service import roadmap, exception

log = getLogger(__name__)


@cache_query(time_limit=60 * 3)  # 3 MINUTE
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
    log.info(graph)
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


@cache_query(caching=False)
async def get_next_modules_by_ids(ids: list[str], limit: int) -> ModulePath:
    cypq = (
        "MATCH (prev:Module)-[:REQUIRES]->(next:Module) "
        "WHERE prev.code IN $ids AND NOT next.code IN $ids "
        "OPTIONAL MATCH (next)-[:INCLUDE]->(skill:Skill) "
        "RETURN next, collect(DISTINCT skill) AS skills "
        "ORDER BY next.code LIMIT $limit;"
    )
    path = await client.get_path(cypq, {"ids": ids, "limit": limit})
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
    log.info(node_ids)
    cypq = (
        "MATCH (m:Module)"
        "WHERE m.code IN $ids "
        "OPTIONAL MATCH (m)-[r]->(other:Module) "
        "WHERE other.code IN $ids "
        "RETURN collect(DISTINCT m) AS modules, collect(r) AS nextRelations;"
    )
    skill = await client.get_graph(cypq, {"ids": node_ids})
    return skill


async def get_skill_details(id: str) -> ModuleDetails:
    skill = await get_skill(id)
    if skill is None:
        raise exception.NotFoundError("module")
    details = await models.ModulesInfo.get_or_none(code=id)
    if details is None:
        raise exception.NotFoundError("module details")

    links = await models.Resource.filter(links__module_code=id).values("title", "url")
    log.debug("links=%s", links)
    return ModuleDetails(
        **skill.model_dump(),
        level=details.level,
        description=details.description,
        links=[Link.model_validate(link) for link in links],
    )
