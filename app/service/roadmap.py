from redis_client.cache import cache_query
from schemas.skill_schema import ModuleOut, ModulePath, SkillOut
from neomodel import adb
from neo4j.graph import Node
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
    "AutomationSpecialization",
]


@cache_query()
async def get_roadmap(from_: list[str], to_: list[str]) -> ModulePath:
    if from_ == []:
        from_ = ["python_syntax_types"]
    cypq = """WITH $modulesOrder AS trackOrder

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
    raw, _ = await adb.cypher_query(
        cypq,
        {"modulesOrder": MODULE_ORDER, "startNodes": from_, "targetNodes": to_},
    )
    path = []
    for row in raw:
        m: Node = row[0]
        skills: list[Node] = row[1]
        path.append(
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
    return ModulePath(path=path)
