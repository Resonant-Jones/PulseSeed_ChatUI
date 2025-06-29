"""Global hotkey management."""
from __future__ import annotations

import threading

import keyboard


class HotkeyManager:
    """Register global hotkeys."""

    def __init__(self) -> None:
        self._running = False

    def start(self) -> None:
        if self._running:
            return
        self._running = True
        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self) -> None:
        keyboard.add_hotkey("ctrl+shift+s", self.on_hotkey)
        keyboard.wait()

    def on_hotkey(self) -> None:  # pragma: no cover - side effect
        print("Hotkey pressed")
