from ...util.structures.Player import Player
from ...util.output import print_info


def interface_effects(player: Player, *args):
    if not args:
        return print_info(str(player.updated_effects), multiline=True)
