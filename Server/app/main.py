import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from services import calculate_sma,calculate_52week,predict_next_day

from .database import Base, engine, get_db
from . import crud, models, services

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

default_tickers = os.getenv("DEFAULT_COMPANIES", "AAPL,MSFT").split(",")

@app.get("/companies")
def get_companies():
    return [{"symbol": t, "name": t} for t in default_tickers]

@app.get("/stock/{symbol}")
def get_stock(symbol: str, db: Session = Depends(get_db)):
    stocks = crud.get_stocks(db, symbol)
    if not stocks:
        data = services.fetch_stock_data(symbol)
        crud.save_stock_data(db, data)
        stocks = crud.get_stocks(db, symbol)
    return stocks

@app.get("/stock/{symbol}")
def get_stock_data(symbol: str, db: Session = Depends(get_db)):
    stocks = crud.get_or_fetch_stocks(db, symbol)
    historical = [{"date": s.date, "close": s.close, "volume": s.volume} for s in stocks]

    closes = [s.close for s in stocks]
    sma_50 = calculate_sma(closes)
    prediction = predict_next_day(historical)
    week_52 = calculate_52week(historical)

    return {
        "historical": historical,
        "sma_50": sma_50,
        "52_week": week_52,
        "prediction": prediction
    }
