from api.auth import auth_router
from api.skills import skill_router
from api.user import user_router
from api.roadmap import path_router
from fastapi import APIRouter

router = APIRouter(prefix="/api")
router.include_router(auth_router)
router.include_router(skill_router)
router.include_router(user_router)
router.include_router(path_router)
