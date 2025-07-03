"""Speech-to-text utilities."""
from __future__ import annotations

import os
from typing import Optional
import httpx

from .config import get_settings
from .logger import logger


async def transcribe(audio_path: str) -> Optional[str]:
    """Return text for an audio file using the configured Whisper API endpoint."""
    settings = get_settings()
    if not settings.enable_stt:
        logger.info("STT is disabled by configuration.")
        return None

    if not settings.whisper_api_url:
        logger.error(
            "Whisper API URL is not set. Please set WHISPER_API_URL in .env"
        )
        return None

    if not os.path.exists(audio_path):
        logger.error("Audio file not found at path: %s", audio_path)
        return None

    try:
        async with httpx.AsyncClient() as client:
            with open(audio_path, "rb") as audio_file:
                files = {"file": (os.path.basename(audio_path), audio_file, "audio/mpeg")} # Assuming mp3, adjust if necessary e.g. "audio/wav"
                # Some Whisper APIs might expect 'audio_file' as the key, or other parameters.
                # This assumes a simple file upload.
                # Add headers if API key is needed for this endpoint, e.g.,
                # headers = {"Authorization": f"Bearer {settings.openai_api_key}"} if it's an OpenAI endpoint
                # For now, assuming no specific auth beyond the URL itself.

                logger.info("Transcribing %s using Whisper API at %s", audio_path, settings.whisper_api_url)
                response = await client.post(settings.whisper_api_url, files=files)
                response.raise_for_status()  # Raises an exception for 4XX/5XX responses

                # Assuming the API returns JSON with a "text" field or "transcription" field
                # This might need adjustment based on the actual API response structure
                response_data = response.json()
                transcribed_text = response_data.get("text") or response_data.get("transcription")

                if transcribed_text:
                    logger.info("Transcription successful: %s", transcribed_text)
                    return transcribed_text
                else:
                    logger.warning("Whisper API response did not contain 'text' or 'transcription' field. Response: %s", response_data)
                    return None

    except httpx.HTTPStatusError as e:
        logger.error(
            "Whisper API request failed with status %s: %s",
            e.response.status_code,
            e.response.text,
        )
        return None
    except httpx.RequestError as e:
        logger.error("Whisper API request failed: %s", e)
        return None
    except Exception as e:
        logger.error("An unexpected error occurred during transcription: %s", e)
        return None
