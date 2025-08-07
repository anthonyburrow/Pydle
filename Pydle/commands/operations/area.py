from ...lib.areas import AREAS
from ...util.Command import Command
from ...util.player.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_area(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        current_area = AREAS[player.area]
        return ui.print(f'{player} is currently at {current_area}.')

    if command.subcommand == 'list':
        msg = []
        msg.append('Available areas:')
        for area in AREAS.values():
            msg.append(f'- {area}')
        return ui.print('\n'.join(msg), multiline=True)

    if command.argument not in AREAS:
        return ui.print(f'{command.argument} is not a valid area.')

    ui.print(AREAS[command.argument].detailed_info(), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- area')
    msg.append('- area list')
    msg.append('- area [area]')

    return '\n'.join(msg)
