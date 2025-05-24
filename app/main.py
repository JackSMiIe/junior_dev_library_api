from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books

app = FastAPI()

# Создаем таблицы в базе (если их нет)
Base.metadata.create_all(bind=engine)

app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Hello, PostgreSQL library API!"}
