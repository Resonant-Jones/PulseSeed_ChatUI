"""Chat bubble widget."""
from __future__ import annotations

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsBlurEffect

from .style import GLASS_BUBBLE
from .components import ToggleButton


class ChatBubble(QtWidgets.QWidget):
    """Floating chat bubble."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(20)
        self.setGraphicsEffect(blur)
        self.setStyleSheet(GLASS_BUBBLE)
        layout = QtWidgets.QVBoxLayout(self)
        self.toggle = ToggleButton("Listen", self)
        layout.addWidget(self.toggle)
        self.input = QtWidgets.QLineEdit(self)
        self.input.setPlaceholderText("Type your message...")
        layout.insertWidget(1, self.input)  # Insert below toggle, above output
        self.output = QtWidgets.QTextEdit("Ready", self)
        self.output.setReadOnly(True)
        self.output.setMinimumHeight(100)
        layout.addWidget(self.output)
