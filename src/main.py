from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title=settings.app_name
)