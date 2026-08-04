from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.schemas.token import Token
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    print("STEP 1")

    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    print("STEP 2")

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    print("STEP 3")

    hashed = hash_password(user.password)

    print("STEP 4", hashed)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed,
    )

    print("STEP 5")

    db.add(new_user)

    print("STEP 6")

    await db.commit()

    print("STEP 7")

    await db.refresh(new_user)

    print("STEP 8")

    return new_user
@router.post(
    "/login",
    response_model=Token,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    existing_user = result.scalar_one_or_none()

    if (
        existing_user is None
        or not verify_password(
            form_data.password,
            existing_user.password,
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    access_token = create_access_token(
        {
            "id": existing_user.id,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }