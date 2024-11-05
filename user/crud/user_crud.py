from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from user.database.databases import get_db
from user.model import models
from user.schemas import schemas

def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
  return db.query(models.User).filter(models.User.id == user_id).first()