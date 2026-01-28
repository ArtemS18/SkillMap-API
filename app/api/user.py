from fastapi import APIRouter, Security
from app.schemas import graph_schema
from schemas import user_schema
from depends import get_current_user_id
from service import progress, skills


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("/progress", response_model=list[str])
async def get_user_learned_skills(
    user_id: int = Security(get_current_user_id, scopes=["me"]),
):
    return await progress.get_learned_skills(user_id)


@user_router.get("/me", response_model=user_schema.OutUser)
async def get_user(
    user_id: int = Security(get_current_user_id, scopes=["me"]),
):
    return await progress.get_user_by_id(user_id)


@user_router.get(
    "/known-skill-graph",
    response_model=graph_schema.GraphGet,
    response_model_by_alias=True,
)
async def get_known_user_skills_graph(
    user_id: int = Security(get_current_user_id, scopes=["me"]),
):
    learned_skiils = await progress.get_learned_skills(user_id)
    g = await skills.get_node_graph(learned_skiils)
    return g
