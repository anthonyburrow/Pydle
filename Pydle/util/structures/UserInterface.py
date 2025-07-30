import traceback
from colorama import just_fix_windows_console

from ..commands import COMMAND_PREFIX
from ..platform import SYS_PLATFORM, Platform


if SYS_PLATFORM == Platform.WINDOWS:
    import win32gui
elif SYS_PLATFORM == Platform.LINUX:
    from Xlib import display as xdisplay


class UserInterface:

    def __init__(self):
        # Allow Colorama/termcolor to work on Windows (does nothing if Unix/Mac)
        just_fix_windows_console()

        self.indent: str = '  '
        self.client_ID: int = self.get_client_ID()

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

    def get_command(self) -> str:
        return input(COMMAND_PREFIX)

    @staticmethod
    def get_client_ID() -> int:
        if SYS_PLATFORM == Platform.WINDOWS:
            return win32gui.GetForegroundWindow()
        elif SYS_PLATFORM == Platform.LINUX:
            d = xdisplay.Display()
            window = d.get_input_focus().focus
            return window.id

    def is_focused(self) -> bool:
        return self.client_ID == self.get_client_ID()


class NullUserInterface(UserInterface):
    def __init__(self):
        pass
    def print(self, message: str): pass
    def print_error(self, message: str): pass
    def get_command(self, prompt: str) -> str:
        return ''
    def get_client_ID(self) -> int:
        return 0
    def client_focused(self) -> bool:
        return True
