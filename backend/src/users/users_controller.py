from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..infra.db import get_db
from .users_manager import get_users, create_user, get_one_user, update_user, delete_user
from .users_schema import UserOut, UserIn, UserUpdate
from uuid import UUID


router = APIRouter(prefix="/users", tags=["users"])

# get all users
@router.get("/", response_model=list[UserOut])
def read_users_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# get one user
@router.get("/{user_id}", response_model=UserOut)
def read_one_user_route(user_id: UUID, db: Session = Depends(get_db)):
    return get_one_user(db, user_id)

# create a user
@router.post("/", response_model=UserOut)
def create_user_route(user: UserIn, db: Session = Depends(get_db)):
    return create_user(db, user)

# update a user
@router.patch("/{user_id}", response_model=UserOut)
def update_user_route(user_id: UUID, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_update)

# delete a user
@router.delete("/{user_id}", status_code=200)
def delete_user_route(user_id: UUID, db: Session = Depends(get_db)):
    return delete_user(db, user_id)

