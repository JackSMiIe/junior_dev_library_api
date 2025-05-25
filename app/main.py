from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books, readers, auth  # добавил auth и readers
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(readers.router, prefix="/readers", tags=["readers"])

@app.get("/")
def read_root():
    return {"message": "Hello, PostgreSQL library API!"}
