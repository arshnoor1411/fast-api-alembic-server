import schemas
import models
from models import User
from database import Base, engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy import func
import bcrypt
import database
from fastapi import APIRouter

app = FastAPI()

router = APIRouter()

@router.post("/signup")
def signup(user: schemas.SignUpModel, session: Session = Depends(database.get_session)):
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hash_password =bcrypt.hashpw(user.password, bcrypt.gensalt())

    new_user = models.User(username=user.username, email=user.email, password=hash_password,createdAt = func.now(), updatedAt = func.now(), deletedAt = func.now() )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message":"user created successfully"}