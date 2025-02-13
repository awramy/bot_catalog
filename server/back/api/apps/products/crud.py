from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Products


async def get_all_products(db: AsyncSession):
    result = await db.execute(select(Products))
    return result.scalars().all()


async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(
        Products.__table__.select().where(Products.id == product_id)
    )
    return result.first()


async def create_product(db: AsyncSession, product_data: dict):
    db_product = Products(**product_data)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def delete_product(db: AsyncSession, product_id: int):
    result = await db.execute(
        Products.__table__.delete().where(Products.id == product_id)
    )
    if result.rowcount == 0:
        return False
    await db.commit()
    return True
