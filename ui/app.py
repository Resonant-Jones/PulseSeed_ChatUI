"""Entry point for the PyQt5 UI."""
from __future__ import annotations
import sys
import requests

from PyQt5 import QtWidgets

from .overlay import Overlay
from .hotkey import HotkeyManager  # Correct single import


def on_hotkey(overlay):
    text = overlay.bubble.input.text()
    send_text_to_backend(text, overlay)
    overlay.bubble.input.clear()


def send_text_to_backend(text: str, overlay):
    url = "http://127.0.0.1:8000/chat"
    try:
        response = requests.post(url, json={"message": text})
        if response.ok:
            reply = response.json().get("reply", "No reply")
            overlay.bubble.output.setText(reply)
            print("Backend response:", reply)
        else:
            overlay.bubble.output.setText(f"API error: {response.status_code}")
            print("Error:", response.status_code)
    except Exception as e:
        overlay.bubble.output.setText(f"Backend request failed: {e}")
        print("Backend request failed:", e)


def main() -> None:  # pragma: no cover - GUI
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()

    hotkeys = HotkeyManager(lambda: on_hotkey(overlay))
    hotkeys.start()

    sys.exit(app.exec_())


if __name__ == "__main__":  # pragma: no cover - direct run
    main()
