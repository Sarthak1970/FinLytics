from sqlalchemy.orm import Session
from . import models, schemas

def save_stock_data(db: Session, stock_data: list[dict]):
    for record in stock_data:
        stock = models.Stock(**record)
        db.add(stock)
    db.commit()

def get_stocks(db: Session, symbol: str, limit: int = 100):
    return db.query(models.Stock).filter(models.Stock.symbol == symbol).order_by(models.Stock.date.desc()).limit(limit).all()
