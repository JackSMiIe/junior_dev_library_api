from sqlalchemy.orm import Session
from app import models, schemas

# Создать новую книгу
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Получить книгу по ID
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Получить список книг с лимитом и смещением
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

# Удалить книгу по ID
def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    update_data = book_update.dict(exclude_unset=True)
    # Проверим, если в update_data есть quantity, что оно не < 0 (защита на уровне crud)
    if 'quantity' in update_data and update_data['quantity'] < 0:
        raise ValueError("Quantity cannot be less than zero")
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book