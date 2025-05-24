from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ----------- User ----------- #

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


# ----------- Book ----------- #

class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    isbn: Optional[str] = None
    quantity: int = 1


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True


# ----------- Reader ----------- #

class ReaderBase(BaseModel):
    name: str
    email: EmailStr


class ReaderCreate(ReaderBase):
    pass


class ReaderRead(ReaderBase):
    id: int

    class Config:
        orm_mode = True


# ----------- BorrowedBook ----------- #

class BorrowedBookBase(BaseModel):
    book_id: int
    reader_id: int
    return_date: Optional[datetime] = None


class BorrowedBookCreate(BorrowedBookBase):
    pass


class BorrowedBookRead(BorrowedBookBase):
    id: int
    borrow_date: datetime

    class Config:
        orm_mode = True
