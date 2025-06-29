"""Waveform display widget."""
from __future__ import annotations

from PyQt5 import QtGui, QtWidgets

from .style import WAVEFORM_COLOR


class Waveform(QtWidgets.QWidget):
    """A placeholder animated waveform."""

    def __init__(self) -> None:
        super().__init__()
        self.level = 0

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:  # noqa: N802
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.QColor(WAVEFORM_COLOR))
        painter.setPen(pen)
        mid = self.height() / 2
        painter.drawLine(0, mid, self.width(), mid)
