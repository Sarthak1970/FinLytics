from pydantic import BaseModel
from datetime import date

class StockBase(BaseModel):
    symbol: str
    date: date
    close: float
    volume: int

class StockCreate(StockBase):
    pass

class StockOut(StockBase):
    class Config:
        orm_mode = True
