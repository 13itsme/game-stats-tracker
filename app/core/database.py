from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

DB_PASS = os.getenv("DB_PASS")

engine = create_async_engine(f"postgresql+asyncpg://postgres:{DB_PASS}@localhost:5432/game-stats-tracker")

sessionmaker = async_sessionmaker(engine, class_=AsyncSession)


class Base(DeclarativeBase):
    pass


async def get_session():
    async with sessionmaker() as session:
        yield session
