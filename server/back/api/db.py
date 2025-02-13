from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from utils import get_db_url


DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine,
                                 class_=AsyncSession,
                                 expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()
