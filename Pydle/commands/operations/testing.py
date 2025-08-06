from ..testing.skilling import testing_skilling
from ...util.Command import Command
from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_testing(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        return ui.print('A subcommand for `testing` is needed.')

    if command.subcommand == 'skilling':
        testing_skilling(player)
    else:
        ui.print(f'Unknown subcommand `{command.subcommand}`')


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- testing skilling')

    return '\n'.join(msg)
