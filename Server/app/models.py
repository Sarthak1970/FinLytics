from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    date = Column(Date, index=True)
    close = Column(Float)
    volume = Column(Integer)
