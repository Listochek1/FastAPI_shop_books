from sqlalchemy import and_, select 
from app.books.models import AuthorsModel, BooksModel, GenreModel
from app.database import new_session
class BaseService:

    model = None

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            result = await session.execute(
                select(cls.model)
            )
            return result.mappings().all()
        
    @classmethod
    async def find_by_id(cls,id):
        async with new_session() as session:
            result = await session.execute(
                select(cls.model).where(cls.model.id == id)
            )
            return result.mappings().all()