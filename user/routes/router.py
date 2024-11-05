from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from user.database.databases import get_db
from user.model.models import User

router = APIRouter(
  prefix='/user'
)

def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
  return db.query(User).filter(User.id == user_id).first()

@router.get('/mypage')
async def get_mypage(user_id: str, db: Session = Depends(get_db)):
  user = get_user_by_id(user_id=user_id, db=db)
  if not user:
    HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="USER NOT FOUND.")
  print(user)
  return user