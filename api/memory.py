"""In-memory conversation store."""
from __future__ import annotations

from typing import List


class ConversationMemory:
    """Simple list-based memory."""

    def __init__(self) -> None:
        self.messages: List[str] = []

    def add(self, text: str) -> None:
        self.messages.append(text)

    def history(self) -> List[str]:
        return self.messages[-50:]


def get_memory() -> ConversationMemory:
    """Return global memory instance."""
    global _MEMORY
    try:
        return _MEMORY
    except NameError:
        _MEMORY = ConversationMemory()
        return _MEMORY
