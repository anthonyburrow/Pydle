from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_bank(player: Player, ui: UserInterface, *args):
    if not args:
        return ui.print(str(player.bank), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- bank')

    return '\n'.join(msg)
