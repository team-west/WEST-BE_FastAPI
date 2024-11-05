from sqlalchemy import Column, VARCHAR, Enum, CHAR
from user.database.enums import genderEnum, stylesEnum
from user.database.databases import Base
from uuid import uuid4
from user.database.databases import engine

class User(Base):
  __tablename__ = "user"

  account_id = Column(CHAR(36), nullable=False, primary_key=True, unique=True, default=lambda: str(uuid4))
  id = Column(VARCHAR(30), nullable=False, primary_key=True, unique=True)
  name = Column(VARCHAR(10), nullable=False)
  number = Column(VARCHAR(20), nullable=False, unique=True)
  password = Column(VARCHAR(100), nullable=False)
  user_gender = Column(Enum(genderEnum), nullable=False)
  user_styles = Column(Enum(stylesEnum), nullable=False)