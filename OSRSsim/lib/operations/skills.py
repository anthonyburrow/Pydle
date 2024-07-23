from ...util.structures import Player
from ...util.output import print_output


def interface_skills(player: Player, *args):
    if not args:
        print_output(player.skills)
        return

    skill = args[0]

    try:
        print_output(player.get_skill(skill))
    except KeyError:
        msg = f'{skill} is not a valid skill.'
        print_output(msg)
