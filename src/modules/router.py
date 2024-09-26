from fastapi import APIRouter

from src.modules.auth.controller import router as auth_router
from src.modules.user.controller import router as user_router

router = APIRouter()

router.include_router(auth_router)
# Auth should always be first

router.include_router(user_router)
