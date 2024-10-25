from pydantic import BaseModel

class User(BaseModel):
  user_name: str
  user_id: str
  user_gender: str
  user_phone_number: str