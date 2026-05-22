from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.crud import get_latest_price
from app.schema import PriceResponse
from app.models import Price

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


@app.get("/prices/latest")
def read_latest_price(ticker: str):
    fake_prices = {
        "BTC": 104233,
        "ETH": 3120,
    }

    return {
        "ticker": ticker,
        "price": fake_prices.get(ticker, 0),
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
def get_prices(ticker: str, db: Session = Depends(get_db)):
    return db.query(Price).filter(Price.ticker == ticker).all()