from jose import jwt, exceptions
from src.settings.exceptions import BadAuthorizationHeaderExceptions
from src.settings.settings import settings


async def get_token_payload(token: str) -> str | dict:
    """Получить email из токена"""
    try:
        token_payload = jwt.decode(token=token, key=settings.token_settings.secret,
                                   algorithms=settings.token_settings.algorithm)
        email = token_payload.get("user_email")
        return email
    except exceptions.JWTError:
        raise BadAuthorizationHeaderExceptions
