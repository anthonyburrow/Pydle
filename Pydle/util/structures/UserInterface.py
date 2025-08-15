from colorama import just_fix_windows_console
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.key_binding import KeyBindings
import traceback


try:
    from pynput import keyboard
except ImportError:
    pass

from .CommandSuggestion import CommandSuggestion
from ..platform import SYS_PLATFORM, Platform


if SYS_PLATFORM == Platform.WINDOWS:
    import win32gui
elif SYS_PLATFORM == Platform.LINUX:
    from Xlib import display as xdisplay


COMMAND_PREFIX: str = '> '
KEY_CANCEL: str = 'c'


BINDINGS = KeyBindings()

@BINDINGS.add('tab')
def _(event):
    b = event.app.current_buffer
    if b.suggestion:
        b.insert_text(b.suggestion.text)
    else:
        b.insert_text('\t')


class UserInterface:

    def __init__(self):
        # Allow Colorama/termcolor to work on Windows (does nothing if Unix/Mac)
        just_fix_windows_console()

        self.indent: str = '  '
        self.client_ID: int = self._get_client_ID()

        self.keyboard_listener = None
        self.activity_running: bool = False

    def print(self, message: str, multiline: bool = False) -> None:
        if not message:
            return

        if not multiline:
            return print(f'{self.indent}{message}')

        message = message.split('\n')
        message = f'\n{self.indent}'.join(message)
        print(f'\n{self.indent}{message}\n')

    def print_error(self, message: str) -> None:
        if not message:
            return

        print(f'Error: {message}')
        print(traceback.format_exc())

    def get_input(self) -> str:
        session: PromptSession = PromptSession(
            auto_suggest=CommandSuggestion(),
            key_bindings=BINDINGS,
            history=InMemoryHistory(max_length=20),
        )
        return session.prompt(COMMAND_PREFIX)

    def flush_input(self):
        try:
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()
        except ImportError:
            # for linux/unix
            import sys
            import termios
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)

    def start_keyboard_listener(self):
        self.keyboard_listener = keyboard.Listener(
            on_release=self._cancel_pressed
        )
        self.keyboard_listener.start()

        self.activity_running = True

    def stop_keyboard_listener(self):
        self.keyboard_listener.stop()
        self.keyboard_listener = None

        self.activity_running = False

    def _cancel_pressed(self, key):
        if not isinstance(key, keyboard.KeyCode):
            return

        if key.char == KEY_CANCEL and self._is_focused():
            self.activity_running = False

    def _is_focused(self) -> bool:
        return self.client_ID == self._get_client_ID()

    @staticmethod
    def _get_client_ID() -> int:
        if SYS_PLATFORM == Platform.WINDOWS:
            return win32gui.GetForegroundWindow()
        elif SYS_PLATFORM == Platform.LINUX:
            d = xdisplay.Display()
            window = d.get_input_focus().focus
            return window.id


class NullUserInterface(UserInterface):
    def __init__(self):
        pass
    def print(self, message: str): pass
    def print_error(self, message: str): pass
    def get_command(self, prompt: str) -> str:
        return ''
    def _get_client_ID(self) -> int:
        return 0
    def client_focused(self) -> bool:
        return True
    def start_keyboard_listener(self): pass
    def stop_keyboard_listener(self): pass
