import yfinance as yf
from datetime import timedelta
import numpy as np
from sklearn.linear_model import LinearRegression


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
            "date": date.date().isoformat(),  
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

    return float(predicted_price)  


def calculate_sma(closes, window=50):
    if len(closes) < window:
        return None
    return float(sum(closes[-window:]) / window)  


def calculate_52week(stocks: list[dict]):
    if not stocks:
        return None
    closes = [s["close"] for s in stocks]
    return {
        "high": float(max(closes)),
        "low": float(min(closes))
    }
