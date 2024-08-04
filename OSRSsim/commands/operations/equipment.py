from ...util.structures.Player import Player
from ...util.output import print_info


def interface_equipment(player: Player, *args):
    if not args:
        return print_info(str(player.equipment), multiline=True)

    subcommand = args[0]

    if subcommand == 'stats':
        return print_info(str(player.stats), multiline=True)

    equippable_name = ' '.join(args[1:])

    if not equippable_name:
        msg = 'An item argument was not given.'
        return print_info(msg)

    if subcommand == 'equip':
        operation = player.equip(equippable_name)
    elif subcommand == 'unequip':
        operation = player.unequip(equippable_name)
    else:
        msg = f'{subcommand} is not a valid argument.'
        return print_info(msg)

    print_info(operation['msg'])


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- equipment')
    msg.append('- equipment equip [item]')
    msg.append('- equipment unequip[item]')
    msg.append('- equipment stats')

    return '\n'.join(msg)
