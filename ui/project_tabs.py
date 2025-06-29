"""Project tabs widget."""
from __future__ import annotations

from PyQt5 import QtWidgets


class ProjectTabs(QtWidgets.QTabWidget):
    """Basic tab container."""

    def __init__(self) -> None:
        super().__init__()
        self.addTab(QtWidgets.QWidget(), "Project 1")
        self.addTab(QtWidgets.QWidget(), "Project 2")
