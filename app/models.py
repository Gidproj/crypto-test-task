from sqlalchemy import Column, Integer, String, Float, BigInteger
from app.database import Base


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(BigInteger)