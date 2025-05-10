import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.whatsapp import whatsapp
from app.utils.logger import log_message
from app.core.settings import settings


VERSION = "v0.1.0"

api_metadata = {
    "title": "WhatsApp API",
    "description": "API para envio e recebimento de mensagens via WhatsApp Cloud",
    "version": VERSION,
}

app = FastAPI(
    title=api_metadata["title"],
    description=api_metadata["description"],
    version=api_metadata["version"],
    docs_url=None if settings.ENV != "dev" else "/docs",
    redoc_url=None if settings.ENV != "dev" else "/redoc",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Lifespan (executado no startup e shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    log_message("INFO", "lifespan", {}, f"Starting app in ENV: {settings.ENV}")
    yield
    log_message("INFO", "lifespan", {}, "Shutting down app.")


app.router.lifespan_context = lifespan

app.include_router(
    whatsapp.router,
    prefix="",
    tags=["whatsapp"],
    responses={404: {"description": "Not found"}},
)


@app.get("/")
def root():
    return {"msg": "API Running Lets Bora!"}
