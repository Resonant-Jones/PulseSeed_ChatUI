"""Text-to-speech utilities."""
from __future__ import annotations

from typing import Optional

from .config import get_settings
from .logger import logger


def speak(text: str) -> Optional[str]:
    """Generate speech if TTS is enabled."""
    settings = get_settings()
    if not settings.enable_tts:
        logger.info("TTS disabled")
        return None

    # Placeholder for real TTS integration
    logger.info("Speaking: %s", text)
    return "audio_path.wav"
