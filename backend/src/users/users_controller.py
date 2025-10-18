from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..infra.db import get_db
from .users_manager import get_users
from .users_schema import UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/test", response_model=list[UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    print('TESTTT')
    return get_users(db, skip=skip, limit=limit)
