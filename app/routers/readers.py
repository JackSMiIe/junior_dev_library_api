from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app import schemas, models, crud
from app.dependencies import get_current_user
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ReaderRead)
def create_reader(reader: schemas.ReaderCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_reader = crud.get_reader_by_email(db, reader.email)
    if db_reader:
        raise HTTPException(status_code=400, detail="Email already registered for reader")
    return crud.create_reader(db, reader)

@router.get("/", response_model=List[schemas.ReaderRead])
def read_readers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_readers(db, skip=skip, limit=limit)

@router.get("/{reader_id}", response_model=schemas.ReaderRead)
def read_reader(reader_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_reader = crud.get_reader(db, reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return db_reader

@router.put("/{reader_id}", response_model=schemas.ReaderRead)
def update_reader(reader_id: int, reader: schemas.ReaderCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_reader = crud.get_reader(db, reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return crud.update_reader(db, reader_id, reader)

@router.delete("/{reader_id}")
def delete_reader(reader_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_reader = crud.get_reader(db, reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    crud.delete_reader(db, reader_id)
    return {"detail": "Reader deleted"}
