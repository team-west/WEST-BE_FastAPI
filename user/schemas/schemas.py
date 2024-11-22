from pydantic import BaseModel, constr, field_validator
from user.database.enums import genderEnum
from fastapi import HTTPException, status

class User(BaseModel):
  id: str
  name: str
  number: str
  password: str
  user_gender: genderEnum
  user_styles: str

  @field_validator('id', 'name', 'number', 'password', 'user_gender', 'user_styles')
  @classmethod
  def check_empty(cls, v):
    if not v or v.isspace():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="필수 항목 입력")
    return v