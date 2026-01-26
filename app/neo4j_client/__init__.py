from neo4j import AsyncGraphDatabase, AsyncDriver
from neo4j.graph import Node, Relationship

from schemas.graph_schema import EdgeGet, GraphGet, NodeGet
from schemas.skill_schema import ModuleOut, ModulePath, SkillOut
from config import settings


class Neo4jClient:
    def __init__(self, uri: str, login: str, pwd: str):
        self.driver: AsyncDriver | None = None

        self.uri = uri
        self.login = login
        self.pwd = pwd

    async def connect(self, *, test_uri: str = ""):
        if test_uri:
            self.driver = AsyncGraphDatabase.driver(
                test_uri, auth=(self.login, self.pwd)
            )
        self.driver = AsyncGraphDatabase.driver(self.uri, auth=(self.login, self.pwd))

    async def execute(self, query: str, params: dict):
        async with self.driver.session() as session:
            res = await session.run(query, params)
            values = []
            async for record in res:
                values.append(tuple(record.values()))
            return values

    async def get_graph(self, query: str, params: dict) -> GraphGet:
        raw = await self.execute(query, params)
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

    async def get_path(self, query: str, params: dict):
        raw = await client.execute(query, params)
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

    async def disconnect(self):
        if self.driver:
            await self.driver.close()


client = Neo4jClient(
    settings.neo4j_connection_string, settings.neo4j_user, settings.neo4j_password
)
