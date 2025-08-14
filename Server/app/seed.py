import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import services, crud

load_dotenv()

def seed():
    db: Session = SessionLocal()
    tickers = os.getenv("DEFAULT_COMPANIES", "AAPL,MSFT").split(",")

    for symbol in tickers:
        print(f"Fetching data for {symbol}...")
        data = services.fetch_stock_data(symbol)
        crud.save_stock_data(db, data)
        print(f"Seeded {symbol}")

    db.close()
    print("Seeding complete!")

if __name__ == "__main__":
    seed()
