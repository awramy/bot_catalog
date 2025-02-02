from pydantic import BaseModel


class BasketCreate(BaseModel):
    user_id: int
    product_id: int
    printImage: str


class Basket(BasketCreate):
    id: int

    class Config:
        orm_mode = True
