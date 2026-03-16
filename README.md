# Crypto Price Service

## Stack
- FastAPI
- PostgreSQL
- Celery
- Docker

## Run
docker compose up --build

## API
- /prices
- /prices/latest
- /prices/by-date

## Design decisions
- Celery for periodic tasks
- PostgreSQL for persistence
- FastAPI for external API
