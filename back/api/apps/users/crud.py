from sqlalchemy.ext.asyncio import AsyncSession

from .models import Users
from .schemas import UserCreate


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(
        Users.__table__.select().where(Users.id == user_id)
    )
    return result.first()


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = Users(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
