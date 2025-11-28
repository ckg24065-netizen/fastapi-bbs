from fastapi import FastAPI
from app.routers import thread
from app.routers import posts

app = FastAPI(
    title="BBS API",
    description="Simple Bulletin Board System API",
    version="0.1"
)

# ルーターを登録（まだ中身は空でOK）
app.include_router(thread.router)
app.include_router(posts.router)
app.include_router(posts.threads_router)
