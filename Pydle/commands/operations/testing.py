from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface
from ..testing.skilling import testing_skilling


def interface_testing(player: Player, ui: UserInterface, *args):
    if not args:
        return ui.print('A subcommand for `testing` is needed.')

    subcommand = args[0]

    if subcommand == 'skilling':
        testing_skilling(player)
    else:
        ui.print(f'Unknown subcommand `{subcommand}`')


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- testing skilling')

    return '\n'.join(msg)
