from typing import Any
from fastapi import HTTPException, status


class DetailedHTTPException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server error"

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail, **kwargs)


class DatabaseExceptions(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Server database exception."


class AuthorizationHeaderExceptions(DetailedHTTPException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Empty authorization header."


class BadAuthorizationHeaderExceptions(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad authorization header."


class UserDontExistExceptions(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "User dont exist."


class BadFileExtensions(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "png, jpg resolution files are allowed"
