import time
import requests
from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.schema import PriceResponse
from app.models import Price

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://your-vercel-app.vercel.app"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/prices/history")
def get_price_history(
    ticker: str = Query(...),
    limit: int = Query(10),
    db: Session = Depends(get_db)
):
    prices = (
        db.query(Price)
        .filter(Price.ticker == ticker)
        .order_by(Price.timestamp.desc())
        .limit(limit)
        .all()
    )

    return list(reversed(prices))


import requests


@app.get("/prices/latest")
def read_latest_price(
    ticker: str,
    db: Session = Depends(get_db)
):

    coin_map = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
    }

    coin_id = coin_map.get(ticker.upper())

    if not coin_id:
        return {"error": "Unsupported ticker"}

    url = (
        f"https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin_id}&vs_currencies=usd"
    )

    response = requests.get(url)
    data = response.json()

    price = data[coin_id]["usd"]

    # сохраняем в БД
    new_price = Price(
        ticker=ticker,
        price=price,
        timestamp=int(time.time())
    )

    db.add(new_price)
    db.commit()

    return {
        "ticker": ticker,
        "price": price,
        "created_at": "2026-01-01T00:00:00"
    }


@app.get("/prices/by-date", response_model=list[PriceResponse])
def get_prices_by_date(
    ticker: str,
    from_ts: int,
    to_ts: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Price)
        .filter(
            Price.ticker == ticker,
            Price.timestamp >= from_ts,
            Price.timestamp <= to_ts
        )
        .all()
    )


@app.get("/prices", response_model=list[PriceResponse])
def get_prices(
    ticker: str,
    db: Session = Depends(get_db)
):
    return db.query(Price).filter(Price.ticker == ticker).all()