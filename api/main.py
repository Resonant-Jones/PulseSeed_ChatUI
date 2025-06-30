"""FastAPI application entry point."""
from __future__ import annotations

from fastapi import FastAPI

from .routes import router
from .logger import logger

app = FastAPI(title="PulseSeed API")
app.include_router(router)


@app.on_event("startup")
async def startup_event() -> None:
    logger.info("PulseSeed API starting up")
