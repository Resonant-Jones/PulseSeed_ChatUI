"""Screen capture utilities."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from PIL import ImageGrab

from .config import get_settings
from .logger import logger


def capture_screen(path: str) -> Optional[Path]:
    """Capture the screen to a given path if enabled."""
    settings = get_settings()
    if not settings.enable_screen_capture:
        logger.info("Screen capture disabled")
        return None

    img = ImageGrab.grab()
    p = Path(path)
    img.save(p)
    logger.info("Captured screen to %s", p)
    return p
