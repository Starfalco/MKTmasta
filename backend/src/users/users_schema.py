from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserIn(BaseModel):
  user_name: str
  email: EmailStr
  is_admin: bool = False,
  password: str

class UserOut(UserIn):
  id: UUID

class UserUpdate(BaseModel):
  user_name: Optional[str] = None
  email: Optional[EmailStr] = None
  is_admin: Optional[bool] = None
  password: Optional[str] = None