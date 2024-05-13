from fastapi import APIRouter, Depends, UploadFile, File
from starlette.requests import Request
from src.user.schemas import DetailedUserSchemas, BaseUserSchemas
from src.user.service import UserService, init_user_service

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/current-profile/", response_model=DetailedUserSchemas)
async def get_current_user_router(request: Request, service: UserService = Depends(
                                  init_user_service)):
    """Роутер информации о текущем пользователе"""
    return await service.get_current_user(request)


@user_router.get("/find-user/", response_model=list[BaseUserSchemas])
async def find_user_router(name: str | None = None, surname: str | None = None,
                           service: UserService = Depends(init_user_service)):
    """Роутер поиска пользователей"""
    return await service.find_user(name, surname)


@user_router.patch("/add-avatar/", response_model=DetailedUserSchemas)
async def add_avatar_router(request: Request, file: UploadFile = File(),
                            service: UserService = Depends(init_user_service)):
    """Роутер добавление аватара"""
    return await service.add_avatar(request=request, avatar=file)
