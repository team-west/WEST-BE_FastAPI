from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from user.database.databases import get_db
from user.model.models import User
from user.database import databases
from user.crud.user_crud import get_user_by_id, get_weather
router = APIRouter(
  prefix='/user'
)

@router.get('/mypage')
async def mypage(user_id: str, db: Session = Depends(get_db)):
  user = get_user_by_id(user_id=user_id, db=db)
  if not user:
    HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="USER NOT FOUND.")
  print(user)
  return user

@router.get('/main')
async def mainpage(latitude: float, longitude: float): #, db: Session = Depends(get_db)):
  weather = get_weather(latitude, longitude)
  if weather == 400:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request For OpenAPI.")
  elif weather == 401:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Don't Have Authorized Token for OpenAPI.")
  elif weather == 403:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized API Token Used for OpenAPI.")
  elif weather == 500:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="OpenAPI SERVER Error.")

  return weather