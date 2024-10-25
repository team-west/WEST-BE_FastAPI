from sqlalchemy import Column, TEXT, str, VARCHAR, Enum
from user.database.enums import genderEnum
from user.database.databases import Base

class User(Base):
  