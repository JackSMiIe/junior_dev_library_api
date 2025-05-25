# 📚 Junior Dev Library API

![REST API](https://img.shields.io/badge/REST-API-blue?style=flat&logo=python)
![JWT Auth](https://img.shields.io/badge/Auth-JWT-green)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)

RESTful API для управления библиотекой книг с аутентификацией пользователей и разграничением доступа.

## 🚀 Быстрый старт

```bash
# Клонирование и установка
git clone https://github.com/JackSMiIe/junior_dev_library_api.git
cd junior_dev_library_api

# Виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Миграции базы данных
alembic upgrade head

# Запуск сервера
uvicorn app.main:app --reload
