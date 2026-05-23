# Crypto Exchange Dashboard 

# Ссылка на сайт: https://crypto-test-task-puce.vercel.app/
Современный фуллстек-сервис для мониторинга криптовалют в реальном времени. Проект сочетает в себе высокую производительность бэкенда на Python и интерактивный пользовательский интерфейс на Next.js.

## 🚀 Основные возможности

* **Мониторинг цен:** Актуальные котировки BTC, ETH и других активов.
* **Интерактивные графики:** Визуализация изменений цен.
* **Bitcoin Clicker:** Игровой элемент для взаимодействия с платформой.
* **Backend:** REST API на FastAPI с поддержкой фоновых задач (Celery + Redis).
* **UI/UX:** Современный дизайн в стиле Glassmorphism.

## 🛠 Технологический стек

### Backend
- **FastAPI:** Высокопроизводительный фреймворк для API.
- **PostgreSQL:** Надежная база данных для хранения данных.
- **SQLAlchemy:** ORM для работы с БД.
- **Celery + Redis:** Фоновые задачи для обновления данных.

### Frontend
- **Next.js 16 (App Router):** Современный React-фреймворк.
- **TypeScript:** Строгая типизация кода.
- **TailwindCSS:** Адаптивная верстка.
- **Recharts:** Интерактивная визуализация данных.

## 📦 Локальный запуск

Для запуска проекта убедитесь, что у вас установлены [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/).

1. Клонируйте репозиторий:
   ```bash
   git clone [https://github.com/Gidproj/crypto-test-task.git](https://github.com/Gidproj/crypto-test-task.git)
   cd crypto-test-task
