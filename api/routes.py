"""API route definitions."""
from __future__ import annotations

from fastapi import APIRouter

from .agent import process_message
from .screen_capture import capture_screen
from .stt import transcribe

router = APIRouter()


@router.post("/chat")
async def chat(message: str) -> dict[str, str]:
    reply = await process_message(message)
    return {"reply": reply}


@router.post("/transcribe")
async def transcribe_audio(path: str) -> dict[str, str | None]:
    text = await transcribe(path)
    return {"text": text}


@router.post("/capture")
async def capture(path: str) -> dict[str, str | None]:
    result = capture_screen(path)
    return {"path": str(result) if result else None}
