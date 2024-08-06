from ...util.structures.Player import Player
from ...util.output import print_info


def interface_effects(player: Player, *args):
    if not args:
        return print_info(str(player.updated_effects), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- effects')

    return '\n'.join(msg)
