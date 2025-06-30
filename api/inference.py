"""Inference engine placeholder."""
from __future__ import annotations

from .logger import logger
from .memory import ConversationMemory


def generate_reply(message: str, memory: ConversationMemory) -> str:
    """Generate a reply from the agent.

    This is a placeholder that simply echoes the last message and memory size.
    """
    logger.info("Generating reply for: %s", message)
    memory.add(message)
    return f"Echo: {message} (history {len(memory.history())})"
