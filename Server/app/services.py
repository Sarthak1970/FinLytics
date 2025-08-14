import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def fetch_stock_data(symbol: str):
    try:
        df = yf.download(symbol, period="1y")
    except Exception as e:
        raise RuntimeError(f"Error fetching data for {symbol}: {str(e)}")
    
    if df.empty:
        raise ValueError(f"No stock data found for {symbol}")

    data = []
    for date, row in df.iterrows():
        data.append({
            "symbol": symbol,
            "date": date.date(),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })
    return data

def predict_next_day(stocks: list[dict]):
    if len(stocks) < 2:
        return None 
    
    stocks_sorted = sorted(stocks, key=lambda x: x["date"])
    X = np.arange(len(stocks_sorted)).reshape(-1, 1)  
    y = np.array([s["close"] for s in stocks_sorted])

    model = LinearRegression()
    model.fit(X, y)

    next_day_index = np.array([[len(stocks_sorted)]])
    predicted_price = model.predict(next_day_index)[0]

    next_date = stocks_sorted[-1]["date"] + timedelta(days=1)

    return {
        "date": next_date.strftime("%Y-%m-%d"),
        "predicted_close": float(predicted_price)
    }

def calculate_sma(closes, window=50):
    if len(closes) < window:
        return None
    return sum(closes[-window:]) / window

def calculate_52week(stocks: list[dict]):
    if len(stocks) < 250:  
        return None

    closes = [s["close"] for s in stocks[-250:]]
    return {
        "high": max(closes),
        "low": min(closes)
    }