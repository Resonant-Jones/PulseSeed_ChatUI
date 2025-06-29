"""Chat bubble widget."""
from __future__ import annotations

from PyQt5 import QtWidgets

from .style import GLASS_BUBBLE
from .components import ToggleButton


class ChatBubble(QtWidgets.QWidget):
    """Floating chat bubble."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(self.windowFlags() | QtWidgets.Qt.Tool)
        self.setStyleSheet(GLASS_BUBBLE)
        layout = QtWidgets.QVBoxLayout(self)
        self.toggle = ToggleButton("Listen", self)
        layout.addWidget(self.toggle)
        self.output = QtWidgets.QLabel("Ready", self)
        layout.addWidget(self.output)
