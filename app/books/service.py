from sqlalchemy import and_, delete, select, update 
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
    @classmethod
    async def deletebook(cls,book_id):
        async with new_session() as session:
            deletebook = await session.execute(delete(BooksModel).where(BooksModel.id == book_id))
            await session.commit()

    @classmethod
    async def update_title_book(cls,book_id,title_book):
        async with new_session() as session:
            updatebook = await session.execute(update(BooksModel).where(BooksModel.id == book_id).values(title =title_book))
            await session.commit()