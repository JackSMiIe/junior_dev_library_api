from app import crud, schemas, models
from app.database import SessionLocal

def test_crud_books():
    db = SessionLocal()

    # Очистка тестовых данных, если книга с таким ISBN уже есть
    existing_book = db.query(models.Book).filter(models.Book.isbn == "1234567890").first()
    if existing_book:
        crud.delete_book(db, book_id=existing_book.id)

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
    assert book.quantity == 5

    # Обновление книги
    book_update = schemas.BookUpdate(
        title="Updated Title",
        author="Updated Author",
        quantity=10
    )
    updated_book = crud.update_book(db, book_id=book.id, book_update=book_update)
    assert updated_book.title == "Updated Title"
    assert updated_book.author == "Updated Author"
    assert updated_book.quantity == 10

    # Проверка обновлённой книги из БД
    fetched_book = crud.get_book(db, book_id=book.id)
    assert fetched_book.title == "Updated Title"

    # Удаление книги
    crud.delete_book(db, book_id=book.id)

    # Проверка, что книга удалена
    deleted_book = crud.get_book(db, book_id=book.id)
    assert deleted_book is None

    db.close()


