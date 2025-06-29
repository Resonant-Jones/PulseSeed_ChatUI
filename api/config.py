"""Configuration loader for PulseSeed."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from .env."""

    groq_api_key: str | None = None
    elevenlabs_api_key: str | None = None
    whisper_api_url: str | None = None

    enable_stt: bool = True
    enable_tts: bool = True
    enable_screen_capture: bool = False
    enable_ui_bubble: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
