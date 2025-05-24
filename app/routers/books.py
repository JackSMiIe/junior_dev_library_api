from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.database import get_db
from app.dependencies import get_current_user  # функция, возвращающая текущего авторизованного пользователя

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(get_current_user)]  # Все эндпоинты защищены JWT
)

@router.post("/", response_model=schemas.BookRead, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    if book.quantity < 0:
        raise HTTPException(status_code=400, detail="Quantity cannot be less than zero")
    db_book = crud.get_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="Book with this ISBN already exists")
    return crud.create_book(db=db, book=book)

@router.get("/", response_model=List[schemas.BookRead])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=schemas.BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book_update.quantity is not None and book_update.quantity < 0:
        raise HTTPException(status_code=400, detail="Quantity cannot be less than zero")
    return crud.update_book(db=db, db_book=db_book, book_update=book_update)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db=db, db_book=db_book)
    return

