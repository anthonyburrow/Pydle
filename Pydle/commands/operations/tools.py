from ...util.structures.Player import Player
from ...util.output import print_info
from ...util.Result import Result


def interface_tools(player: Player, *args):
    if not args:
        print_info(str(player.tools), multiline=True)
        return

    subcommand = args[0]
    tool = ' '.join(args[1:])

    if not tool:
        msg = 'A tool argument was not given.'
        print_info(msg)
        return

    if subcommand == 'equip':
        result: Result = player.equip_tool(tool)
    elif subcommand == 'unequip':
        result: Result = player.unequip_tool(tool)
    else:
        msg = f'{subcommand} is not a valid argument.'
        print_info(msg)
        return

    print_info(result.msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- tools')
    msg.append('- tools equip [tool]')
    msg.append('- tools unequip [tool]')

    return '\n'.join(msg)
