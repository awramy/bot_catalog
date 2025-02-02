from sqlalchemy import Column, Integer, String, Float, JSON

from db import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)
    pattern = Column(JSON, nullable=False)
