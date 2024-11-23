from fastapi import FastAPI

from app.api.routers.avatar import router as avatar_router
from app.api.routers.item import router as item_router
from app.api.routers.quest import router as quest_router
from app.api.routers.user import router as user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(quest_router)
app.include_router(item_router)
app.include_router(avatar_router)
