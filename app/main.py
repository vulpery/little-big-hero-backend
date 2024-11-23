from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.avatar import router as avatar_router
from app.api.routers.item import router as item_router
from app.api.routers.quest import router as quest_router
from app.api.routers.user import router as user_router

app = FastAPI()

# Specify origins allowed to make requests
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://little-big-hero.vulpery.com",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only specified origins
    allow_credentials=True,  # Allow cookies to be included in requests
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user_router)
app.include_router(quest_router)
app.include_router(item_router)
app.include_router(avatar_router)
