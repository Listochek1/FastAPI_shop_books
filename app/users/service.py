from sqlalchemy import and_, select 
from app.users.models import UsersModel
from app.database import new_session



class UserService():
    @classmethod
    async def find_by_login(cls,login):
        async with new_session() as session:
            results = await session.execute(select(UsersModel.id).where(UsersModel.login == login))

            return results.scalar_one_or_none()