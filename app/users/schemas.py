from pydantic import BaseModel
from datetime import date
class UserModel(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True

