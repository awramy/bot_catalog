from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import create_user, get_user
from .schemas import User, UserCreate
from db import get_db


router = APIRouter()


@router.get("/user", response_model=User)
async def one_user(
        user_id: int = Header(..., alias="id"),
        db: AsyncSession = Depends(get_db)
    ):
    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/user/", response_model=User)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await create_user(db, user=user)
    return user
