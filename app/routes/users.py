from fastapi import APIRouter, Depends

from app.core.oauth2 import get_current_user
from app.schemas.token import TokenData

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
async def get_me(
    current_user: TokenData = Depends(get_current_user),
):
    return {
        "message": "Authenticated!",
        "user_id": current_user.id,
    }