from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from src.settings.settings import settings

engine = create_async_engine(settings.database_settings.database_full_url, echo=False)

async_engine = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
