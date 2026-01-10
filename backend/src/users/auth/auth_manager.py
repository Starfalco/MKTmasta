from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from ..users_model import Users
from .auth_schema import RegisterIn, LoginIn
from ...common.security import hash_password, verify_password, create_access_token

def register(db: Session, data: RegisterIn):
    # Check if he exists
    exists = db.query(Users).filter(
        or_(Users.email == data.email, Users.user_name == data.user_name)
    ).first()

    if exists:
        raise HTTPException(status_code=409, detail="Email or username already used")

    user = Users(
        user_name=data.user_name,
        email=data.email,
        password=hash_password(data.password),
        is_admin=False,
    )

    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email or username already used")

    db.refresh(user)
    return user


def login(db: Session, data: LoginIn) -> str:
    user = db.query(Users).filter(Users.email == data.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return create_access_token(subject=str(user.id))
