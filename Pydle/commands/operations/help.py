from ..Action import Action
from ..Command import InvalidCommandError
from ..CommandRegistry import COMMAND_REGISTRY, CMD_EXIT
from ..Command import Command
from ..Operation import Operation
from ...util.colors import color, color_theme
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
        msg.append('- help')
        msg.append('- help [command]')

        return '\n'.join(msg)

    def execute(self) -> None:
        if self.command.argument:
            try:
                command_action: type[Action] = \
                    Command.get_action(self.command.argument)
                self.ui.print(command_action.usage(), multiline=True)
            except InvalidCommandError:
                self.ui.print(f"No help available for '{self.command.argument}'.")

            return

        msg: list[str] = []

        command_str = color(self.name, color_theme['UI_1'])
        msg.append(f'Use `{command_str} [command]` for more detail on a command.')

        msg.append('')
        msg.append('Operations:')

        for command_name, command_action in COMMAND_REGISTRY.operations.items():
            if command_name == 'testing':
                continue

            command_str = color(command_name, color_theme['UI_1'])

            alias_str: str = ''
            if command_action.aliases:
                alias_str = ', '.join([
                    color(alias, color_theme['UI_1'])
                    for alias in command_action.aliases
                ])
                alias_str = f'({alias_str}) '

            msg.append(f'  - {command_str} {alias_str}: {command_action.help_info}')

        msg.append('')
        msg.append('Activities:')

        for command_name, command_action in COMMAND_REGISTRY.activities.items():
            command_str = color(command_name, color_theme['UI_1'])

            alias_str: str = ''
            if command_action.aliases:
                alias_str = ', '.join([
                    color(alias, color_theme['UI_1'])
                    for alias in command_action.aliases
                ])
                alias_str = f'({alias_str}) '

            msg.append(f'  - {command_str} {alias_str}: {command_action.help_info}')

        msg.append('')
        msg.append('Other:')

        command_str = color(KEY_CANCEL, color_theme['UI_1'])
        msg.append(f'  - Press "{command_str}" to cancel an ongoing activity.')

        command_str = color(CMD_EXIT, color_theme['UI_1'])
        msg.append(f'  - {command_str}: Exit the game.')

        self.ui.print('\n'.join(msg), multiline=True)
