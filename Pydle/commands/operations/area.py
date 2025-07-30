from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface
from ...lib.areas import AREAS


def interface_area(player: Player, ui: UserInterface, *args):
    if not args:
        current_area = AREAS[player.area]
        return ui.print(f'{player} is currently at {current_area}.')

    subcommand = ' '.join(args)

    if subcommand == 'list':
        msg = []
        msg.append('Available areas:')
        for area_key, area in AREAS.items():
            msg.append(f'- {area}')
        return ui.print('\n'.join(msg), multiline=True)

    if subcommand not in AREAS:
        return ui.print(f'{subcommand} is not a valid area.')

    ui.print(AREAS[subcommand].detailed_info(), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- area')
    msg.append('- area list')
    msg.append('- area [area]')

    return '\n'.join(msg)
