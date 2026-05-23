import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker
import random
import time

# 1. Подключаем SQLite 
SQLALCHEMY_DATABASE_URL = "sqlite:///./crypto.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель под таблицу
class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(BigInteger)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. Настраиваем CORS для Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crypto-test-task-puce.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Эмуляция Celery
async def mock_crypto_parser():
    while True:
        db = SessionLocal()
       
        new_price = Price(
            ticker="BTC", 
            price=random.uniform(60000.0, 65000.0), 
            timestamp=int(time.time())
        )
        db.add(new_price)
        db.commit()
        db.close()
        await asyncio.sleep(60) 

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(mock_crypto_parser())

# 4. Эндпоинт для фронта
@app.get("/prices/latest")
def get_latest_price(ticker: str = "BTC"):
    db = SessionLocal()
    latest = db.query(Price).filter(Price.ticker == ticker).order_by(Price.timestamp.desc()).first()
    db.close()
    if latest:
        return {"ticker": latest.ticker, "price": latest.price, "timestamp": latest.timestamp}
    return {"error": "No data found"}