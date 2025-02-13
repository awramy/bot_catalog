from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey

from db import Base


class Baskets(Base):
    __tablename__ = "baskets"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger,
                    ForeignKey("users.id", ondelete="CASCADE"),
                    nullable=False)
    product_id = Column(Integer,
                        ForeignKey("products.id", ondelete="CASCADE"),
                        nullable=False)
    printImage = Column(String, nullable=False)
