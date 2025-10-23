from sqlalchemy.orm import Session
from .users_model import Users
from .users_schema import UserIn, UserUpdate
from fastapi import HTTPException, status
from uuid import UUID
import bcrypt

# CENTRALISER GESTION ERREURS AVEC SQL PAR LA SUITE DS UN EXCEPTION.PY!!

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def get_users(db: Session, skip: int = 0, limit: int = 10):
    # db: Session → type hint pour autocomplétion et clarté (session SQLAlchemy injectée via get_db)
    # skip (offset) → nombre de lignes à ignorer (utile pour pagination)
    # limit → nombre max de résultats retournés (ex: 10 users par page)

    return db.query(Users).offset(skip).limit(limit).all()

def get_one_user(db: Session, user_id: UUID):
    user = db.get(Users, user_id)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def create_user(db: Session, user: UserIn):
    db_user = Users(
        user_name=user.user_name, 
        email=user.email,
        password = hash_password(user.password),
        is_admin=user.is_admin,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: UUID, user_update: UserUpdate):
    user = db.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    update_data = user_update.model_dump(exclude_unset=True)

    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    for key, value in update_data.items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: UUID):
    print("DELETE MANAGER")
    user = db.get(Users, user_id)
    
    if not user:
        raise HTTPException(404, "User not found for the delete")
    
    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}