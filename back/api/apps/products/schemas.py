from pydantic import BaseModel
from typing import Dict

class ProductCreate(BaseModel):
    name: str
    price: float
    image: str
    description: str
    pattern: dict

class Product(ProductCreate):
    id: int

    class Config:
        orm_mode = True
