import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker
import random
import time

# Подключаем SQLite
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

# Настраиваем CORS для Vercel (без слеша на конце!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crypto-test-task-puce.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Эмуляция фоновой задачи (теперь генерируем и BTC, и ETH)
async def mock_crypto_parser():
    while True:
        db = SessionLocal()
        current_time = int(time.time())
        
        # Добавляем BTC
        btc_price = Price(
            ticker="BTC", 
            price=random.uniform(60000.0, 65000.0), 
            timestamp=current_time
        )
        # Добавляем ETH
        eth_price = Price(
            ticker="ETH", 
            price=random.uniform(3000.0, 3200.0), 
            timestamp=current_time
        )
        
        db.add(btc_price)
        db.add(eth_price)
        db.commit()
        db.close()
        
        await asyncio.sleep(60) # Обновляем раз в минуту

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(mock_crypto_parser())

# Эндпоинт для последней цены (для карточек)
@app.get("/prices/latest")
def get_latest_price(ticker: str = "BTC"):
    db = SessionLocal()
    latest = db.query(Price).filter(Price.ticker == ticker).order_by(Price.timestamp.desc()).first()
    db.close()
    if latest:
        return {"ticker": latest.ticker, "price": latest.price, "timestamp": latest.timestamp}
    return {"error": "No data found"}

# НОВЫЙ: Эндпоинт для графика (история цен)
@app.get("/prices/history")
def get_price_history(ticker: str = "BTC", limit: int = 20):
    db = SessionLocal()
    # Берем последние N записей
    history = db.query(Price).filter(Price.ticker == ticker).order_by(Price.timestamp.desc()).limit(limit).all()
    db.close()
    
    # Разворачиваем список, чтобы старые данные были слева, а новые справа (как на графиках)
    history.reverse()
    
    return [{"timestamp": item.timestamp, "price": item.price} for item in history]