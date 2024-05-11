from datetime import date
from pydantic import BaseModel


class BaseUserSchemas(BaseModel):
    """Базовая схема пользователей"""
    name: str
    surname: str
    city: str


class DetailedUserSchemas(BaseUserSchemas):
    """Подробная информация о пользователе"""
    status: str | None = None
    description: str
    birthday: date
