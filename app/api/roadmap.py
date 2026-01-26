from fastapi import APIRouter, Security
from depends import get_current_user_id
from schemas import skill_schema
from service import progress
from gigachat.client import gigachat_client


path_router = APIRouter(prefix="/my-roadmap", tags=["My Roadmap"])


@path_router.post("/create", response_model=skill_schema.UserPath)
async def create_user_path(
    schema: skill_schema.UserPromt,
    user_id: int = Security(get_current_user_id, scopes=["roadmap.write"]),
):
    raw = await gigachat_client.send_roadmap_promt(schema.message)
    path_info = skill_schema.CreateRoadmapSchema.model_validate(raw)
    return await progress.create_user_path(user_id, path_info)


@path_router.get("/", response_model=skill_schema.UserPath)
async def get_user_path(
    user_id: int = Security(get_current_user_id, scopes=["roadmap.read"]),
):
    return await progress.get_current_user_path(user_id)


@path_router.get("/{code}/next-step", response_model=skill_schema.ModuleOut)
async def get_next_step_in_user_path(
    code: str,
    user_id: int = Security(get_current_user_id, scopes=["roadmap.read"]),
):
    return await progress.get_next_step(code, user_id)


@path_router.post("/{code}/complite", response_model=skill_schema.UserPath)
async def complite_module(
    code: str,
    user_id: int = Security(get_current_user_id, scopes=["roadmap.write"]),
):
    return await progress.update_progress(user_id, code)
