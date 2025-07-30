from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_effects(player: Player, ui: UserInterface, *args):
    if not args:
        return ui.print(str(player.updated_effects), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- effects')

    return '\n'.join(msg)
