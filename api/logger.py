"""Simple application logger."""
from __future__ import annotations

import logging
from pathlib import Path

LOG_PATH = Path("logs/daemon.log")
LOG_PATH.parent.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("PulseSeed")
