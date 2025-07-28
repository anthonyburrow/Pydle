from ...util.structures.Player import Player
from ...util.output import print_info
from ...lib.areas import areas


def interface_area(player: Player, *args):
    if not args:
        current_area = areas[player.area]
        return print_info(f'{player} is currently at {current_area}.')

    subcommand = ' '.join(args)

    if subcommand == 'list':
        msg = []
        msg.append('Available areas:')
        for area in areas:
            name = str(area).capitalize()
            msg.append(f'- {name}')
        return print_info('\n'.join(msg), multiline=True)

    if subcommand not in areas:
        return print_info(f'{subcommand} is not a valid area.')

    print_info(areas[subcommand].detailed_info(), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- area')
    msg.append('- area list')
    msg.append('- area [area]')

    return '\n'.join(msg)
