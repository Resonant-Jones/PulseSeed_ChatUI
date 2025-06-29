"""Reusable UI components."""
from __future__ import annotations

from PyQt5 import QtWidgets


class ToggleButton(QtWidgets.QPushButton):
    """A simple on/off toggle."""

    def __init__(self, label: str, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(label, parent)
        self.setCheckable(True)
