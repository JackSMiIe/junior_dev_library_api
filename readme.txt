# 📚 Junior Dev Library API

![Python](https://img.shields.io/badge/Python-3.7+-blue) 
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green) 
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red) 
![JWT](https://img.shields.io/badge/Auth-JWT-orange) 
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-blueviolet)

RESTful API для управления библиотекой книг с аутентификацией пользователей и разграничением доступа.

## 🚀 Быстрый старт

### Установка и запуск

<pre>
1. Клонирование репозитория
   git clone https://github.com/JackSMiIe/junior_dev_library_api.git
   cd junior_dev_library_api

2. Создание виртуального окружения
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows

3. Установка зависимостей
   pip install -r requirements.txt

4. Настройка базы данных (создайте файл .env с переменными окружения)
   DATABASE_URL=postgresql://user:password@localhost:5432/library_db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Применение миграций
   alembic upgrade head

6. Запуск сервера
   uvicorn app.main:app --reload
</pre>

