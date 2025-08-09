from typing import Type

from ..CommandRegistry import COMMAND_REGISTRY
from ...util.colors import color, color_theme
from ...util.Command import CMD_EXIT
from ...util.structures.CommandBase import CommandBase
from ...util.structures.Operation import Operation
from ...util.structures.UserInterface import KEY_CANCEL


class HelpOperation(Operation):

    name: str = 'help'
    aliases: list[str] = ['?', 'h']
    subcommands: list[str] = []
    help_info: str = 'Show the list of available commands.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append(f'- help')
        msg.append(f'- help [command]')

        return '\n'.join(msg)

    def execute(self) -> None:
        if self.command.argument:
            command_cls: Type[CommandBase] | None = \
                COMMAND_REGISTRY.get(self.command.argument)

            if command_cls:
                self.ui.print(command_cls.usage())
            else:
                self.ui.print(f"No help available for '{self.command.argument}'.")

            return

        msg: list[str] = []

        command_str = color(self.name, color_theme['UI_1'])
        msg.append(f'Use `{command_str} [command]` for more detail on a command.')

        msg.append('')
        msg.append('Operations:')

        for command_name, command_cls in COMMAND_REGISTRY.operations.items():
            if command_name == 'testing':
                continue

            command_str = color(command_name, color_theme['UI_1'])

            alias_str: str = ''
            if command_cls.aliases:
                alias_str = [
                    color(alias, color_theme['UI_1'])
                    for alias in command_cls.aliases
                ]
                alias_str = ', '.join(alias_str)
                alias_str = f"({alias_str}) "

            msg.append(f"  - {command_str} {alias_str}: {command_cls.help_info}")

        msg.append('')
        msg.append('Activities:')

        for command_name, command_cls in COMMAND_REGISTRY.activities.items():
            command_str = color(command_name, color_theme['UI_1'])

            alias_str: str = ''
            if command_cls.aliases:
                alias_str = [
                    color(alias, color_theme['UI_1'])
                    for alias in command_cls.aliases
                ]
                alias_str = ', '.join(alias_str)
                alias_str = f"({alias_str}) "

            msg.append(f"  - {command_str} {alias_str}: {command_cls.help_info}")

        msg.append('')
        msg.append('Other:')

        command_str = color(KEY_CANCEL, color_theme['UI_1'])
        msg.append(f'  - Press "{command_str}" to cancel an ongoing activity.')

        command_str = color(CMD_EXIT, color_theme['UI_1'])
        msg.append(f'  - {command_str}: Exit the game.')

        self.ui.print('\n'.join(msg), multiline=True)
