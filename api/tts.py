"""Text-to-speech utilities."""
from __future__ import annotations

import os
import tempfile
from typing import Optional
from elevenlabs import Voice, VoiceSettings
from elevenlabs.client import ElevenLabs, APIError

from .config import get_settings
from .logger import logger


def speak(text: str) -> Optional[str]:
    """Generate speech using the configured TTS engine and return the audio file path."""
    settings = get_settings()
    if not settings.enable_tts:
        logger.info("TTS is disabled by configuration.")
        return None

    if settings.tts_engine == "elevenlabs":
        if not settings.elevenlabs_api_key:
            logger.error(
                "ElevenLabs API key is not set. Please set ELEVENLABS_API_KEY in .env"
            )
            return None

        try:
            client = ElevenLabs(api_key=settings.elevenlabs_api_key)
            # TODO: Make voice ID and model configurable if needed
            audio_iterator = client.generate(
                text=text,
                voice=Voice(
                    voice_id="Rachel", # Example voice ID, consider making this configurable
                    settings=VoiceSettings(
                        stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True
                    ),
                ),
                model="eleven_multilingual_v2", # Or other desired model
                stream=False # Get all audio at once
            )

            # Save audio to a temporary file
            # Using a temporary file for simplicity. For production, consider a more robust storage.
            fd, temp_audio_path = tempfile.mkstemp(suffix=".mp3")
            os.close(fd) # Close the file descriptor opened by mkstemp

            with open(temp_audio_path, "wb") as f:
                for chunk in audio_iterator:
                    f.write(chunk)

            logger.info("Generated speech and saved to: %s", temp_audio_path)
            return temp_audio_path

        except APIError as e:
            logger.error("ElevenLabs API error: %s", e)
            return None
        except Exception as e:
            logger.error("An unexpected error occurred during TTS generation: %s", e)
            return None

    else:
        logger.warning(
            "Unsupported TTS engine: %s. No audio will be generated.",
            settings.tts_engine,
        )
        return None
