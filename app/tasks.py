import time
from app.config import celery_app
from app.deribit_client import get_prices_from_deribit
from app.database import SessionLocal, engine, Base
from app.models import Price


@celery_app.task
def fetch_prices():

    db = SessionLocal()

    prices = get_prices_from_deribit()

    for ticker, price in prices.items():
        new_price = Price(
            ticker=ticker,
            price=float(price),
            timestamp=int(time.time())
        )
        db.add(new_price)

    db.commit()
    db.close()