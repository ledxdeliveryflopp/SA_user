from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Настройки для БД"""
    user: str
    postgres_password: str
    host: str
    port: str
    database_name: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_full_url(self):
        return (f'postgresql+asyncpg://{self.user}:{self.postgres_password}@{self.host}:'
                f'{self.port}/{self.database_name}')


class TokenSettings(BaseSettings):
    """Настройки для токенов"""
    secret: str
    algorithm: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Settings(BaseSettings):
    """Набор всех настроек"""
    database_settings: DatabaseSettings
    token_settings:  TokenSettings


@lru_cache
def init_settings():
    return Settings(database_settings=DatabaseSettings(), token_settings=TokenSettings())


settings = init_settings()
