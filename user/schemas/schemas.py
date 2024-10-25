from pydantic import BaseModel, constr, field_validator
from user.database.enums import genderEnum
from fastapi import HTTPException, status

class User(BaseModel):
  id: constr(max_length=30)
  name: constr(min_length=2, max_length=10)
  number: constr(min_length=13, max_length=13)
  password: constr(max_length=100)
  user_gender: genderEnum
  user_styles: str

  @field_validator('id', 'name', 'number', 'password', 'user_gender', 'user_styles')
  @classmethod
  def check_empty(cls, v):
    if not v or v.isspace():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="필수 항목 입력")
    return v