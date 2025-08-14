import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine, get_db
from . import crud, services
from .services import calculate_sma, calculate_52week, predict_next_day

load_dotenv()

app = FastAPI()
Base.metadata.create_all(bind=engine)

default_tickers = os.getenv("DEFAULT_COMPANIES", "AAPL,MSFT").split(",")

origins = [
    "http://localhost:3000",   
    "http://localhost:5173",   
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "https://fin-lytics-8a99ob4hw-sarthak-katiyars-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],           
    allow_headers=["*"],            
)


@app.get("/companies")
def get_companies():
    """Return the list of available companies."""
    return [{"symbol": t, "name": t} for t in default_tickers]


@app.get("/stock/{symbol}/raw")
def get_stock(symbol: str, db: Session = Depends(get_db)):
    """Return raw stock data from DB (fetch if missing)."""
    stocks = crud.get_stocks(db, symbol)
    if not stocks:
        data = services.fetch_stock_data(symbol)
        crud.save_stock_data(db, data)
        stocks = crud.get_stocks(db, symbol)
    return stocks


@app.get("/stock/{symbol}")
def get_stock_data(symbol: str, db: Session = Depends(get_db)):
    try:
        stocks = crud.get_or_fetch_stocks(db, symbol)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))

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
