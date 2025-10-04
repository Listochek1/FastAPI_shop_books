from pydantic import BaseModel
from datetime import date
class BookResponse(BaseModel):
    first_name: str
    last_name: str
    genre_title: str
    book_title: str
    date_publication: date

    class Config:
        orm_mode = True



class BookIDResponse(BaseModel):

    result : BookResponse



class BookUpdateResponse(BaseModel):
    id : int
    title : str

    
    class Config:
        orm_mode = True