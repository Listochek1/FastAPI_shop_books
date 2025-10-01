from sqlalchemy import and_, select 
from app.baseservice import BaseService
from app.books.models import AuthorsModel, BooksModel, GenreModel
from app.database import new_session



class BooksService(BaseService):
    model = BooksModel
    @classmethod    
    async def get_info(cls):
        async with new_session() as session:
            results = await session.execute(select(
                AuthorsModel.first_name,
                AuthorsModel.last_name,
                GenreModel.title.label('genre_title'),
                BooksModel.title.label('book_title'),
                BooksModel.date_publication
                ).where(and_(AuthorsModel.id == BooksModel.id,
                            BooksModel.genre == GenreModel.id)))
            return results.mappings().all()