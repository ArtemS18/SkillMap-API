import asyncio
from schemas.skill_schema import ModuleOut, ModulePath, SkillOut
from schemas.graph_schema import GraphGet, NodeGet, EdgeGet
from neomodel import adb
from neo4j.graph import Node, Relationship
from neo4j_client import models

MODULE_ORDER = [
    "LanguageCore",
    "AdvancedLanguage",
    "DataAndOS",
    "TestingAndQuality",
    "AsyncAndConcurrency",
    "Databases",
    "WebBackend",
    "Infrastructure",
    "BackendSpecialization",
    "DataSpecialization",
    "AutomationSpecialization"
]

async def get_graph_by_topic(topic: str) -> GraphGet:
    cypq =(
        "MATCH (:Subject{code: $topic_code})-[:LEARN]->(root:Module)"
        "MATCH (root)-[n:REQUIRES*0..]->(m:Module)"
        "OPTIONAL MATCH (m)-[inc:INCLUDE*]->(s:Skill) "
        "RETURN collect(DISTINCT m) AS modules, collect(DISTINCT s) AS skills, collect(DISTINCT n) as nextRelations, collect(DISTINCT inc) AS includeRelations;"
    )
    raw, _ = await adb.cypher_query(cypq, {"topic_code": topic})
    row: tuple[list[Node], list[Node], list[tuple[Relationship, ...]], list[tuple[Relationship, ...]]] = raw[0]
    modules, skills, next_rel, inc_rel = row

    modules_nd = [NodeGet.from_neo4j(m) for m in modules]
    skills_nd = [NodeGet.from_neo4j(m) for m in skills]
    next_edg = [EdgeGet.from_neo4j(m) for m in next_rel if m != []]
    inc_edg = [EdgeGet.from_neo4j(m) for m in inc_rel if m != []]

    return GraphGet(
        nodes=modules_nd + skills_nd,
        edges=next_edg + inc_edg
    )


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
            skills=[SkillOut(
                id=s._properties.get("code"), 
                name=s._properties.get("name")
            ) for s in skills])
        )
    return ModulePath(path=roadmap)

async def get_path_beetwen_modules(from_id: str, to_id: str) -> ModulePath:
    cypq = (
        """WITH $modulesOrder AS trackOrder

        WITH $startNodes AS startCodes,
            $targetNodes AS targetCode,
            trackOrder

        MATCH (s:Module)
        WHERE s.code IN startCodes
        OPTIONAL MATCH (k:Module)-[:REQUIRES*0..]->(s)
        WITH targetCode, collect(DISTINCT k) AS known, trackOrder

        MATCH (t:Module)
        WHERE t.code IN targetCode
        OPTIONAL MATCH path = (dep:Module)-[:REQUIRES*0..]->(t)
        OPTIONAL MATCH (dep)-[:INCLUDE]->(s:Skill)
        WITH dep, max(length(path)) AS depth, known, trackOrder, collect(DISTINCT s) as skills, head([l IN labels(dep) WHERE l <> "Module"]) AS track
        WHERE dep IS NOT NULL AND NOT dep IN known

        RETURN dep, skills, depth
        ORDER BY apoc.coll.indexOf(trackOrder, track), depth DESC;
    """
    )
    raw, _ = await adb.cypher_query(cypq, {
        "modulesOrder": MODULE_ORDER, 
        "startNodes": [from_id], 
        "targetNodes": [to_id]
        }
    )
    path = []
    for row in raw:
        m: Node = row[0]
        skills: list[Node] = row[1]
        path.append(
            ModuleOut(
            id=m._properties.get("code"),
            name=m._properties.get("name"),
            skills=[SkillOut(
                id=s._properties.get("code"), 
                name=s._properties.get("name")
            ) for s in skills])
        )
    return ModulePath(path=path)