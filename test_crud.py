from app import crud, schemas, models
from app.database import SessionLocal

def test_crud_books():
    db = SessionLocal()

    # Очистка тестовых данных (если уже есть)
    existing_book = crud.get_book_by_isbn(db, isbn="1234567890")
    if existing_book:
        crud.delete_book(db, db_book=existing_book)

    # Создание книги
    book_in = schemas.BookCreate(
        title="Test Book",
        author="Test Author",
        year=2020,
        isbn="1234567890",
        quantity=5
    )
    book = crud.create_book(db, book=book_in)
    assert book.id is not None
    assert book.title == "Test Book"

    # Удаление после теста (опционально)
    crud.delete_book(db, db_book=book)
    db.close()

