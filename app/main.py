from fastapi import FastAPI
from typing import List,Dict
from datetime import date, datetime
from fastapi import HTTPException,status,Response,Request

from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
from sqlalchemy import Date, DateTime, ForeignKey, Integer, String,DATE, and_, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.books.shemas import BookResponse,BookIDResponse,BookUpdateResponse
from app.books.service import BooksService

from app.users.auth import Auth
from app.users.schemas import UserModel
from app.settings import Settings
from app.users.service import UserService
import datetime


app = FastAPI()


@app.get("/")
async def get_main():
    """end_point для получения информации о всех книгах"""
    return {"msg":"Hello World"}

@app.get("/books/getinfobook")
async def get_info_book():
    """end_point для получения информации о всех книгах"""
    return await BooksService.get_info()

@app.get("/books/getallbooks")
async def get_allbooks():
    """end_point для получения информации о всех книгах"""
    return await BooksService.get_all()


        
@app.get("/books/{book_id}/")
async def get_book(book_id : int,request:Request):
    """end point для получения книг по id"""
    try:
        acces_token = request.cookies.get("acces_token")
        data = await Auth.dec_token(acces_token,Settings.JWT_SECRET_KEY,Settings.ALGORITHM)
        exp = data["exp"]
        date_now = int(datetime.datetime.utcnow().timestamp())
        if exp>date_now:
            return await BooksService.find_by_id(book_id)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/users/register/")
async def registration(user: UserModel):
    """endpoint для регистрации пользователя"""
    password_hash = await Auth.get_password_hash(user.password)
    return await Auth.registration(login=user.login,password=password_hash)


@app.post("/users/login/")
async def login(user: UserModel,response:Response):
    """endpoint для входа"""
    password = user.password
    if await Auth.verify_password(password=password,login=user.login):
        id = await UserService.find_by_login(user.login)
        iat = datetime.datetime.utcnow()
        exp = iat + datetime.timedelta(minutes=30)
        token = await Auth.create_token(payload={"sub":f"{id}","username":user.login,"iat":iat,"exp":exp},SECRET_KEY=Settings.JWT_SECRET_KEY,ALGORITHM=Settings.ALGORITHM) 
        response.set_cookie(key="acces_token",value=token,httponly=True,secure=True)
        return {"acces_token":token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid login or password")


@app.post("/users/logout/")
async def login(response:Response):
    return response.delete_cookie("acces_token")



@app.get("/users/protected")
async def protected_endpoint(request:Request):
    """endpoint для проверки наличия jwt токена"""
    try:
        acces_token = request.cookies.get("acces_token")
        data = await Auth.dec_token(acces_token,Settings.JWT_SECRET_KEY,Settings.ALGORITHM)
        exp = data["exp"]
        date_now = int(datetime.datetime.utcnow().timestamp())
        if exp>date_now:
            return await BooksService.get_info()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

@app.delete("/books/deletebooks/{book_id}")
async def delete_book(book_id : int):
    result = await BooksService.deletebook(book_id)
    if result:
        return {"detail":"книга удалена"}
    else:
        {"detail":"ошибка: книга не удалена"}

@app.put("/books/update/title/")
async def update_book(body:BookUpdateResponse):
    book_id = body.id
    title_book = body.title
    try:
        await BooksService.update_title_book(book_id,title_book)
        return {"detail":True}
    except:
        return None
