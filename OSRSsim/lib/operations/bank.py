from ...util.structures import Player
from ...util.output import print_output


def interface_bank(player: Player, *args):
    if not args:
        print_output(player.bank)
        return
