from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .crud import get_product, get_all_products, create_product, delete_product
from .schemas import ProductCreate, Product
from db import get_db


router = APIRouter()


@router.get("/products", response_model=List[Product])
async def all_products(db: AsyncSession = Depends(get_db)):
    products = await get_all_products(db)
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products


@router.post("/products", response_model=Product)
async def create_new_product(
        product: ProductCreate,
        db: AsyncSession = Depends(get_db)
    ):
    db_product = await create_product(db, product_data=product.dict())
    return db_product


@router.get("/products/{product_id}", response_model=Product)
async def one_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/products/{product_id}")
async def delete_product_endpoint(product_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_product(db, product_id=product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
