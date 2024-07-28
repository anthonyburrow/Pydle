from ...util.structures.Player import Player
from ...util.output import print_info


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

    if subcommand == 'add':
        operation = player.add_tool(tool)
    elif subcommand == 'remove':
        operation = player.remove_tool(tool)
    else:
        msg = f'{subcommand} is not a valid argument.'
        print_info(msg)
        return

    print_info(operation['msg'])
