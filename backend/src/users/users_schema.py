from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    user_name: str
    email: str