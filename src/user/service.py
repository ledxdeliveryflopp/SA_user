from dataclasses import dataclass
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from src.settings.depends import get_session
from src.settings.exceptions import AuthorizationHeaderExceptions, UserDontExistExceptions
from src.user.models import UserModel
from src.user.repository import UserRepository
from src.user.utils import get_token_payload


@dataclass
class UserService(UserRepository):
    """Сервис пользователей"""

    async def get_current_user(self, request: Request) -> UserModel or dict:
        """Информация о текущем пользователе по токену"""
        header_token = request.headers.get("Authorization")
        if not header_token:
            raise AuthorizationHeaderExceptions
        header_token = header_token.replace("Bearer ", "")
        token_payload = await get_token_payload(header_token)
        user = await self.get_user_by_token_payload(token_payload)
        if not user:
            raise UserDontExistExceptions
        return user

    async def find_user(self, name: str, surname: str) -> UserModel or dict:
        """Поиск пользователя по name или surname"""
        user = await self.find_user_by_name_or_surname(name, surname)
        if not user:
            raise UserDontExistExceptions
        return user


async def init_user_service(session: AsyncSession = Depends(get_session)):
    """Инициализация сервиса пользователей"""
    return UserService(session)

