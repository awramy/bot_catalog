from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .schemas import Basket
from .crud import get_basket, delete_all_basket, delete_one_from_basket
from db import get_db


router = APIRouter()


@router.get("/basket", response_model=List[Basket])
async def full_basket(
        user_id: int = Header(..., alias="user_id"),
        db: AsyncSession = Depends(get_db)
    ):
    basket = await get_basket(db, user_id)
    if not basket:
        raise HTTPException(status_code=404, detail="Basket is empty")
    return basket


@router.delete("/basket")
async def clear_basket(
        user_id: int = Header(..., alias="user_id"),
        db: AsyncSession = Depends(get_db)
    ):
    success = await delete_all_basket(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Basket not found")
    return {"message": "Basket cleared successfully"}


@router.delete("/basket/{product_id}")
async def delete_one_product_from_basket(
        product_id: int,
        user_id: int = Header(..., alias="user_id"),
        db: AsyncSession = Depends(get_db)
    ):
    success = await delete_one_from_basket(db, user_id, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Basket not found")
    return {"message": "Basket cleared successfully"}
