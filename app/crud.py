from sqlalchemy.orm import Session
from app.models import Price

def get_latest_price(db: Session, ticker: str):
    return (
        db.query(Price)
        .filter(Price.ticker == ticker)
        .order_by(Price.timestamp.desc())
        .first()
    )

def get_prices(db, ticker: str):
    return db.query(Price).filter(Price.ticker == ticker).all()
