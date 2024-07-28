from ...util.structures.Player import Player
from ...util.output import print_info


def interface_bank(player: Player, *args):
    if not args:
        print_info(str(player.bank), multiline=True)
        return
