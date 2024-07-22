from ...util.structures import Player
from ...util.output import print_output


def interface_stats(player: Player, *args):
    if not args:
        print_output(player.stats)
        return

    stat = args[0]

    try:
        print_output(player.get_stat(stat))
    except KeyError:
        msg = f'{stat} is not a valid stat.'
        print_output(msg)
