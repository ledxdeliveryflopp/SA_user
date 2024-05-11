from src.settings.database import async_engine


async def get_session():
    """Генерации сессии БД"""
    async with async_engine() as session:
        yield session
