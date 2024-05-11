from dataclasses import dataclass
from sqlalchemy import Select, or_
from src.settings.service import BaseService
from src.user.models import UserModel


@dataclass
class UserRepository(BaseService):
    """Репозиторий пользователей"""

    async def get_user_by_token_payload(self, email: str) -> UserModel:
        """Информация о текущем пользователе по email из токена"""
        user = await self.session.execute(Select(UserModel).where(UserModel.email == email))
        return user.scalar()

    async def find_user_by_name_or_surname(self, name: str, surname: str) -> UserModel:
        """Поиск пользователя по имени или фамилии"""
        users = await self.session.execute(Select(UserModel).where(or_(UserModel.name == name,
                                                                       UserModel.surname == surname)))
        return users.scalars()
