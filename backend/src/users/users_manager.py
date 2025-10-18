from sqlalchemy.orm import Session
from .users_model import Users

def get_users(db: Session, skip: int = 0, limit: int = 10):
    # db: Session → type hint pour autocomplétion et clarté (session SQLAlchemy injectée via get_db)
    # skip (offset) → nombre de lignes à ignorer (utile pour pagination)
    # limit → nombre max de résultats retournés (ex: 10 users par page)
    print('TESTTT')
    return db.query(Users).offset(skip).limit(limit).all()

# def get_user_by_id(db: Session, user_id: int):
#     return db.query(models.Users).filter(models.Users.id == user_id).first()
