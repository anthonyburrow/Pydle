from ...util.structures.Player import Player
from ...util.output import print_info


def interface_skills(player: Player, *args):
    if not args:
        print_info(str(player.skills), multiline=True)
        return

    skill = args[0]

    try:
        print_info(player.get_skill(skill).details())
    except KeyError:
        msg = f'{skill} is not a valid skill.'
        print_info(msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- skills')
    msg.append('- skills [skill]')

    return '\n'.join(msg)
