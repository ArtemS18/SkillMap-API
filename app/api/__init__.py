#from api.user import user_router
from api.auth import auth_router
from api.skills import skill_router
from fastapi import APIRouter

router = APIRouter(prefix="/api")
router.include_router(auth_router)
router.include_router(skill_router)

