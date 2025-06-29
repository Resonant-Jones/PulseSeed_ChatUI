"""Entry point for the PyQt5 UI."""
from __future__ import annotations

import sys

from PyQt5 import QtWidgets

from .overlay import Overlay
from .hotkey import HotkeyManager


def main() -> None:  # pragma: no cover - GUI
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()

    hotkeys = HotkeyManager()
    hotkeys.start()

    sys.exit(app.exec_())


if __name__ == "__main__":  # pragma: no cover - direct run
    main()
