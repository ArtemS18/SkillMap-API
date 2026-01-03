from fastapi import APIRouter, Body, Depends, Security
from depends import get_current_user_id
from service import progress


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("/progress", response_model=list[str])
async def get_user_learned_skills(
    user_id: int = Security(get_current_user_id, scopes=["me"]),
):
    return await progress.get_learned_skills(user_id)
