"""Overlay window managing the chat bubble."""
from __future__ import annotations

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from .bubble import ChatBubble

class Overlay(QtWidgets.QWidget):
    """Full-screen transparent overlay to host the bubble."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.bubble = ChatBubble()
        layout.addWidget(self.bubble)
