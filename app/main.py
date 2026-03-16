from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.crud import get_latest_price
from app.schema import PriceResponse
from app.models import Price

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/prices/latest", response_model=PriceResponse)
def read_latest_price(ticker: str, db: Session = Depends(get_db)):
    return get_latest_price(db, ticker)


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