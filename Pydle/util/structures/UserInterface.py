import traceback
from colorama import just_fix_windows_console

from ..commands import COMMAND_PREFIX


class UserInterface:

    def __init__(self):
        # Allow Colorama/termcolor to work on Windows (does nothing if Unix/Mac)
        just_fix_windows_console()

        self.indent: str = '  '

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


class NullUserInterface(UserInterface):
    def __init__(self):
        pass
    def print(self, message: str): pass
    def print_error(self, message: str): pass
    def get_command(self, prompt: str) -> str:
        return ''
