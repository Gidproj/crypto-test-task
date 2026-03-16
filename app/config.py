from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

celery_app.conf.beat_schedule = {
    "fetch-prices-every-60-seconds": {
        "task": "app.tasks.fetch_prices",
        "schedule": 60.0,
    },
}

celery_app.conf.timezone = "UTC"