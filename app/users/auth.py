import asyncio
from sqlalchemy import and_, insert, select 
from app.users.models import UsersModel
from app.database import new_session
from passlib.context import CryptContext
import bcrypt
import jwt


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


class Auth:
    @classmethod
    async def get_password_hash(cls, password: str) -> str:
        return pwd_context.hash(password,salt="q"*22)
    @classmethod
    async def registration(cls,login,password):
        async with new_session() as session:
            user = await session.execute(select(UsersModel).where(UsersModel.login == login))
            existing_user = user.scalar_one_or_none()
            if existing_user:
                return {"detail": "User with this login already exists"}
            else:
                await session.execute(insert(UsersModel).values(login=login,password=password))
                await session.commit()
                return {"detail":"Registration was successful"}
            


    @classmethod
    async def verify_password(cls,password,login) ->bool:
        async with new_session() as session:
            hashed_password = await session.execute(
                select(UsersModel.password,UsersModel.login).where(UsersModel.login == login)
            )
            hash = hashed_password.scalar_one_or_none()
            print(pwd_context.verify(password, hash))
            return pwd_context.verify(password, hash)
    
    @classmethod
    async def create_token(cls,payload:dict,SECRET_KEY:str,ALGORITHM:str):
        encoded = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
        return encoded
    
    @classmethod
    async def dec_token(cls,token:str,SECRET_KEY:str,ALGORITHM:str):
        decoded_token = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded_token
        
        
        