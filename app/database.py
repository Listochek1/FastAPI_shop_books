from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
# подключение к БД
from app.settings import Settings


engine = create_async_engine(f"postgresql+asyncpg://{Settings.user_db}:{Settings.password}@localhost/{Settings.database}",echo=True)

new_session = async_sessionmaker(engine,expire_on_commit=False,)