"""In-memory conversation store."""
from __future__ import annotations

from typing import List, Dict, Literal

MessageRole = Literal["user", "assistant", "system"]

class Message(Dict):
    role: MessageRole
    content: str

class ConversationMemory:
    """Stores conversation history with roles."""

    def __init__(self, system_prompt: str | None = None, max_history_len: int = 50) -> None:
        self.messages: List[Message] = []
        self.max_history_len = max_history_len
        if system_prompt:
            self.messages.append(Message(role="system", content=system_prompt))

    def add_message(self, role: MessageRole, content: str) -> None:
        """Adds a message to the history."""
        self.messages.append(Message(role=role, content=content))
        # Optional: Trim history if it exceeds max_history_len, keeping system prompt
        if len(self.messages) > self.max_history_len:
            # Keep system prompt if present, then trim older messages
            if self.messages[0]["role"] == "system":
                self.messages = [self.messages[0]] + self.messages[-(self.max_history_len-1):]
            else:
                self.messages = self.messages[-self.max_history_len:]


    def add_user_message(self, content: str) -> None:
        """Adds a user message to the history."""
        self.add_message(role="user", content=content)

    def add_assistant_message(self, content: str) -> None:
        """Adds an assistant message to the history."""
        self.add_message(role="assistant", content=content)

    def history(self) -> List[Message]:
        """Returns the recent conversation history."""
        # The trimming logic is now within add_message, so history just returns current messages.
        return self.messages

    def get_formatted_history_for_groq(self) -> List[Dict[str, str]]:
        """Returns the history formatted for Groq API (list of dicts with 'role' and 'content')."""
        return [{"role": msg["role"], "content": msg["content"]} for msg in self.history()]

    def clear(self, system_prompt: str | None = None) -> None:
        """Clears the memory, optionally keeping/setting a system prompt."""
        self.messages = []
        if system_prompt:
            self.messages.append(Message(role="system", content=system_prompt))

_MEMORY_INSTANCE: ConversationMemory | None = None

def get_memory(system_prompt: str | None = "You are a helpful assistant.") -> ConversationMemory:
    """Return global memory instance, initializing if necessary."""
    global _MEMORY_INSTANCE
    if _MEMORY_INSTANCE is None:
        # You could load the system_prompt from config here if desired
        _MEMORY_INSTANCE = ConversationMemory(system_prompt=system_prompt)
    return _MEMORY_INSTANCE
