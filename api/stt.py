"""Speech-to-text utilities."""
from __future__ import annotations

from typing import Optional

from .config import get_settings
from .logger import logger


async def transcribe(audio_path: str) -> Optional[str]:
    """Return text for an audio file if STT is enabled."""
    settings = get_settings()
    if not settings.enable_stt:
        logger.info("STT disabled")
        return None

    # Placeholder for real STT integration
    logger.info("Transcribing %s", audio_path)
    return "Transcribed text from " + audio_path
