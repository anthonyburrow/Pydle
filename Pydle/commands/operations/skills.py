from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_skills(player: Player, ui: UserInterface, *args):
    if not args:
        return ui.print(str(player.skills), multiline=True)

    skill = args[0]

    try:
        ui.print(player.get_skill(skill).details())
    except KeyError:
        ui.print(f'{skill} is not a valid skill.')


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- skills')
    msg.append('- skills [skill]')

    return '\n'.join(msg)
