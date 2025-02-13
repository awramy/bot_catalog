from sqlalchemy import Column, BigInteger, String, Float

from db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String(5), default="USER")
    balance = Column(Float)
