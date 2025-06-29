"""Status indicator widget."""
from __future__ import annotations

from PyQt5 import QtWidgets


class StatusIndicator(QtWidgets.QLabel):
    """Simple colored status indicator."""

    def __init__(self) -> None:
        super().__init__("●")
        self.set_status(False)

    def set_status(self, active: bool) -> None:
        color = "green" if active else "red"
        self.setStyleSheet(f"color: {color}; font-size: 18px;")
