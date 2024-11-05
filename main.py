from fastapi import FastAPI
from user.routes import router as mypage_router

app = FastAPI()

app.include_router(mypage_router.router, tags=['USER'])

if __name__ == "__main__":
  from user.database.databases import init_db
  init_db()
  import uvicorn
  uvicorn.run("main:app", host='0.0.0.0', port=2952, reload=True)

# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base, Session
# from pydantic import BaseModel

# # FastAPI 인스턴스 생성
# app = FastAPI()

# # 데이터베이스 연결 URL 설정
# DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/mydatabase"

# # SQLAlchemy 엔진 및 세션 생성
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # 베이스 클래스 생성
# Base = declarative_base()

# # 데이터베이스 모델 정의
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     email = Column(String(100))
#     age = Column(Integer)

# # Pydantic 모델 정의
# class UserResponse(BaseModel):
#     id: int
#     name: str
#     email: str
#     age: int

#     class Config:
#         orm_mode = True

# # 의존성 주입을 위한 DB 세션 함수
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # 특정 ID에 해당하는 유저 정보 가져오기
# @app.get("/users/{user_id}", response_model=UserResponse)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
