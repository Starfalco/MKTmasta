from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...infra.db import get_db

from .auth_schema import RegisterIn, RegisterOut, LoginIn, TokenOut
from .auth_manager import register, login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=RegisterOut, status_code=201)
def register_route(data: RegisterIn, db: Session = Depends(get_db)):
    register(db, data)
    return {"message": "Registration successful. You can now sign in."}

@router.post("/login", response_model=TokenOut)
def login_route(data: LoginIn, db: Session = Depends(get_db)):
    print('on print poto')
    token = login(db, data)
    return {"access_token": token, "token_type": "bearer"}

