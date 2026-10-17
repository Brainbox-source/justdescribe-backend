from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import tickets
from .core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

app.include_router(tickets.router)
