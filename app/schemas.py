from pydantic import BaseModel, EmailStr, conint, ConfigDict
from typing import Optional
from datetime import datetime

# ----------- User ----------- #

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ----------- Book ----------- #

class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    isbn: Optional[str] = None
    quantity: conint(ge=0) = 1

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    quantity: Optional[int]
    model_config = ConfigDict(from_attributes=True)


# ----------- Reader ----------- #

class ReaderBase(BaseModel):
    name: str
    email: EmailStr

class ReaderCreate(ReaderBase):
    pass

class ReaderRead(ReaderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)
