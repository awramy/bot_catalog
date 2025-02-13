from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Baskets


async def get_basket(db: AsyncSession, user_id: int):
    result = await db.execute(
        Baskets.__table__.select().where(Baskets.user_id == user_id)
    )
    return result.all()


async def delete_all_basket(db: AsyncSession, user_id: int):
    result = await db.execute(
        Baskets.__table__.delete().where(Baskets.user_id == user_id)
    )
    if result.rowcount == 0:
        return False
    await db.commit()
    return True


async def delete_one_from_basket(db: AsyncSession, user_id: int, product_id: int):
    result = await db.execute(
        Baskets.__table__.delete().where(Baskets.user_id == user_id, Baskets.product_id == product_id)
    )
    if result.rowcount == 0:
        return False
    await db.commit()
    return True
