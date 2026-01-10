from pydantic import BaseModel, EmailStr

class RegisterIn(BaseModel):
    user_name: str
    email: EmailStr
    password: str

class RegisterOut(BaseModel):
    message: str

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"