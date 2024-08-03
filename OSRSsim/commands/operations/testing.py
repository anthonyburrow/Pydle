from ...util.structures.Player import Player
from ...util.output import print_info
from ..testing.skilling import testing_skilling


def interface_testing(player: Player, *args):
    if not args:
        msg = 'A subcommand for `testing` is needed.'
        print_info(msg)
        return

    subcommand = args[0]

    if subcommand == 'skilling':
        testing_skilling(player)
    else:
        msg = f'Unknown subcommand `{subcommand}`'
        print_info(msg)
