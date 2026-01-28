from fastapi import APIRouter, Depends, Query
from schemas import graph_schema, skill_schema
from service import skills as skill_service
from depends import get_current_user_id, request_limit


skill_router = APIRouter(prefix="/skill-graph", tags=["Skills"])


@skill_router.get(
    "/",
    response_model=graph_schema.GraphGet,
    dependencies=[Depends(request_limit(10)), Depends(get_current_user_id)],
)
async def handel_graph_skills(topic: str = Query(...)):
    return await skill_service.get_graph_by_topic(topic)


@skill_router.get("/{id}/next-steps", response_model=skill_schema.ModulePath)
async def handel_next_step(id: str):
    return await skill_service.get_next_modules(id)


@skill_router.get("/{id}", response_model=skill_schema.ModuleOut)
async def handel_get_skill(id: str):
    return await skill_service.get_skill(id)


@skill_router.get("/{from_id}/path-to/{to_id}", response_model=skill_schema.ModulePath)
async def handel_path_to(from_id: str, to_id: str):
    return await skill_service.get_path_beetwen_modules(from_id, to_id)
