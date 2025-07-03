"""Inference engine for LLM interaction."""
from __future__ import annotations

from groq import Groq, APIError
from .logger import logger
from .memory import ConversationMemory
from .config import get_settings


def generate_reply(message: str, memory: ConversationMemory) -> str:
    """Generate a reply from the agent using the configured LLM engine."""
    settings = get_settings()
    logger.info("Generating reply for: %s using LLM: %s", message, settings.llm_engine)

    memory.add_user_message(message) # Add user message to memory

    if settings.llm_engine == "groq":
        if not settings.groq_api_key:
            logger.error("Groq API key is not set. Please set GROQ_API_KEY in .env")
            return "Error: Groq API key not configured."

        client = Groq(api_key=settings.groq_api_key)
        messages_for_api = memory.get_formatted_history_for_groq()

        try:
            chat_completion = client.chat.completions.create(
                messages=messages_for_api,
                model="llama3-8b-8192",  # Or allow model selection via config
            )
            reply = chat_completion.choices[0].message.content
            if reply:
                memory.add_assistant_message(reply) # Add assistant reply to memory
                logger.info("Groq reply: %s", reply)
                return reply
            else:
                logger.warning("Groq returned an empty reply.")
                return "I received an empty response from the LLM."
        except APIError as e:
            logger.error("Groq API error: %s", e)
            return f"Error communicating with Groq API: {e.message}"
        except Exception as e:
            logger.error("An unexpected error occurred while calling Groq API: %s", e)
            return "An unexpected error occurred while generating a reply."

    else:
        logger.warning(
            "Unsupported LLM engine: %s. Falling back to echo.", settings.llm_engine
        )
        # Fallback echo reply if no supported engine is configured
        reply = f"Echo: {message} (history {len(memory.history())})"
        memory.add_assistant_message(reply) # Also add echo reply to memory
        return reply
