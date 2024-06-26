from fastapi import FastAPI

from src.comments.routers import router as comments_router
from src.config import settings
from src.events.routers import router as events_router
from src.reservations.routers import router as reservations_router
from src.users.routers import router as users_router
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache
from redis import asyncio as aioredis
from fastapi_cache.decorator import cache
import time
from fastapi import WebSocket

app = FastAPI(
    title=settings.app_name
)

app.include_router(users_router)
app.include_router(events_router)
app.include_router(reservations_router)
app.include_router(comments_router)

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.redis_host}:{settings.redis_port}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@app.get('/lunghissima')
@cache(expire=30)
async def verylong():
    time.sleep(3)
    return {'key': "ce l'ho fatta"}

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text("You sent this message:"+data)