# ui/hotkey.py
from pynput import keyboard

class HotkeyManager:
    def __init__(self, action=None):
        self.listener = None
        self.action = action or self.do_nothing

    def do_nothing(self):
        pass

    def start(self):
        COMBO = {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode.from_char('s')}
        current = set()

        def on_press(key):
            if key in COMBO:
                current.add(key)
                if all(k in current for k in COMBO):
                    self.action()

        def on_release(key):
            try:
                current.remove(key)
            except KeyError:
                pass

        self.listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        self.listener.start()