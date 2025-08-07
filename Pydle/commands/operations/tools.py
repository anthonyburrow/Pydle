from ...util.Command import Command
from ...util.Result import Result
from ...util.items.ItemInstance import ItemInstance
from ...util.items.ItemParser import ITEM_PARSER
from ...util.items.Tool import Tool
from ...util.player.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_tools(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        return ui.print(str(player.tools), multiline=True)

    if not command.argument:
        return ui.print('A tool argument was not given.')

    if command.quantity != 1:
        return ui.print('Only one item can be equipped or unequipped at a time.')

    item_instance: ItemInstance | None = command.get_item_instance()

    if not item_instance:
        return ui.print(f"Item '{command.argument}' is not a valid argument.")

    if not isinstance(item_instance.base, Tool):
        return ui.print(f"Item '{item_instance}' is not equippable.")

    if command.subcommand == 'equip':
        result: Result = player.equip_tool(item_instance)
    elif command.subcommand == 'unequip':
        result: Result = player.unequip_tool(item_instance)

    ui.print(result.msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- tools')
    msg.append('- tools equip [tool]')
    msg.append('- tools unequip [tool]')

    return '\n'.join(msg)
