from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from src.user.router import user_router

user_microservice = FastAPI()


user_microservice.include_router(user_router)

user_microservice.mount("/static", StaticFiles(directory="static"), name="static")