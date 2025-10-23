from ..infra.db import Base
from sqlalchemy import Column, Integer, String, Boolean
import uuid

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, default=uuid.uuid4)
    user_name = Column(String(120), nullable=False, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

