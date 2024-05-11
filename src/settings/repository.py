from dataclasses import dataclass
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession
from src.settings.exceptions import DatabaseExceptions


@dataclass
class BaseRepository:
    """Базовый репозиторий для работы с БД"""
    session: AsyncSession

    async def session_save_object(self, saved_object: object) -> dict:
        """Сохранение объекта в бд"""
        try:
            self.session.add(saved_object)
            await self.session.commit()
            await self.session.refresh(saved_object)
        except IntegrityError:
            raise DatabaseExceptions
        except ProgrammingError:
            raise DatabaseExceptions

    async def session_delete_object(self, deleted_object: object) -> dict:
        """Удаление объекта из БД"""
        try:
            await self.session.delete(deleted_object)
            await self.session.commit()
        except IntegrityError:
            raise DatabaseExceptions
        except ProgrammingError:
            raise DatabaseExceptions



