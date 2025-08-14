from sqlalchemy.orm import Session
from . import models, services

def get_stocks(db: Session, symbol: str):
    return db.query(models.Stock).filter(models.Stock.symbol == symbol).all()

def save_stock_data(db: Session, data: list):
    for item in data:
        stock = models.Stock(
            symbol=item["symbol"],
            date=item["date"],
            close=item["close"],
            volume=item["volume"]
        )
        db.add(stock)
    db.commit()

def get_or_fetch_stocks(db: Session, symbol: str):
    stocks = get_stocks(db, symbol)
    if stocks:
        return stocks

    data = services.fetch_stock_data(symbol)
    save_stock_data(db, data)
    return get_stocks(db, symbol)
