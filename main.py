from fastapi import FastAPI
from src.user.router import user_router

user_microservice = FastAPI()


user_microservice.include_router(user_router)
