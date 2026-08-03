from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/")
async def auth_root():
    return {
        "message": "Authentication route ready."
    }