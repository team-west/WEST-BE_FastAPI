from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from user.database.databases import get_db
from user.model.models import User
from user.schemas import schemas
from user.model import models

def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
  return db.query(models.User).filter(models.User.id == user_id).first()

import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(latitude, longitude):
  url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}"

  response = requests.get(url)
  if response == 400:
    return 400
  elif response == 401:
    return 401
  elif response == 403:
    return 403
  elif response == 404:
    return 404
  elif response == 500:
    return 500
  contexts = response.text
  contents = json.loads(contexts)
  city = contents['city']['name']
  if city == "Daejeon":
    city = '대전'
  elif city == "Seoul":
    city = '서울'
  elif city == "Sejong":
    city = '세종'
  elif city == "Gwacheon":
    city = "과천"
  elif city == "Gwangmyeong":
    city = "광명"
  else:
    city = "대한민국"

  weather = contents['list'][2]['weather'][0]['main']
  if weather == "Clear":
    weather = '맑음'
  elif weather == "Rain":
    weather = '비'
  elif weather == "Clouds":
    weather = '구름'
  else:
    weather = '맑음'

  weather_detail = contents['list'][2]['weather'][0]['description']
  if weather_detail == "light rain":
    weather_detail = '가벼운 비'
  elif weather_detail == "moderate rain":
    weather_detail = "적당한 비"
  elif weather_detail == "scattered clouds":
    weather_detail = '흩어진 구름'
  elif weather_detail == "few clouds":
    weather_detail = "구름 거의 없음"
  elif weather_detail == "broken clouds":
    weather_detail = ''
  elif weather_detail == "overcast clouds":
    weather_detail = '빽빽한 구름'
  elif weather_detail == "clear sky":
    weather_detail = "맑은 하늘"
  else:
    weather_detail = "맑은 하늘"

  temperature = contents['list'][2]['main']['temp']
  temperature = temperature - 270.15

  temperature_min = contents['list'][2]['main']['temp_min']
  temperature_min = temperature_min - 270.15

  temperature_max = contents['list'][2]['main']['temp_max']
  temperature_max = temperature_max - 270.15

  return {'city': city, 'weather': weather, 'weather_detail': weather_detail, 'temp': temperature, 'temp_min': temperature_min, 'temp_max': temperature_max}