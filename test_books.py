from app import crud, schemas, models
from app.database import SessionLocal

def test_create_and_delete_book():
    db = SessionLocal()

    # Удаляем тестовую книгу, если есть
    existing = db.query(models.Book).filter(models.Book.isbn == "0987654321").first()
    if existing:
        crud.delete_book(db, book_id=existing.id)

    # Создание новой книги
    book_in = schemas.BookCreate(
        title="Another Test Book",
        author="Author Name",
        year=2021,
        isbn="0987654321",
        quantity=3
    )
    book = crud.create_book(db, book=book_in)
    assert book.id is not None
    assert book.isbn == "0987654321"

    # Удаляем книгу
    crud.delete_book(db, book_id=book.id)

    # Проверяем, что книга удалена
    deleted = crud.get_book(db, book_id=book.id)
    assert deleted is None

    db.close()

