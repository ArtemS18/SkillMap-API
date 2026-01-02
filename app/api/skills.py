from fastapi import APIRouter, Query
from schemas import graph_schema, skill_schema
from service import skills as skill_service


skill_router = APIRouter(prefix="/skills", tags=["Skills"])


@skill_router.get("/graph", response_model=graph_schema.GraphGet)
async def handel_graph_skills(topic: str = Query(...)):
    return await skill_service.get_graph_by_topic(topic)


@skill_router.get("/{id}/next-steps", response_model=skill_schema.ModulePath)
async def handel_next_step(id: str):
    return await skill_service.get_next_modules(id)


@skill_router.get("/{from_id}/path-to/{to_id}", response_model=skill_schema.ModulePath)
async def handel_path_to(from_id: str, to_id: str):
    return await skill_service.get_path_beetwen_modules(from_id, to_id)
