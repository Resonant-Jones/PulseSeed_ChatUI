"""Agent orchestration functions."""
from __future__ import annotations

from .logger import logger
from .memory import get_memory
from .inference import generate_reply
from .tts import speak


async def process_message(message: str) -> str:
    """Process a user message and return agent reply."""
    memory = get_memory()
    reply = generate_reply(message, memory)
    audio = speak(reply)
    if audio:
        logger.info("Generated speech: %s", audio)
    return reply
