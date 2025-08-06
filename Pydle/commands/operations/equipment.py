from ...util.Result import Result
from ...util.Command import Command
from ...util.ItemParser import ITEM_PARSER
from ...util.items.Item import ItemInstance
from ...util.items.Equippable import Equippable
from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_equipment(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        return ui.print(str(player.equipment), multiline=True)

    if command.subcommand == 'stats':
        return ui.print(str(player.stats), multiline=True)

    if not command.argument:
        return ui.print('An item argument was not given.')

    if command.quantity != 1:
        return ui.print('Only one item can be equipped or unequipped at a time.')

    item_instance: ItemInstance | None = ITEM_PARSER.get_instance(command)

    if not item_instance:
        return ui.print(f"Item '{command.argument}' is not a valid argument.")

    if not isinstance(item_instance.base, Equippable):
        return ui.print(f"Item '{item_instance}' is not equippable.")

    if command.subcommand == 'equip':
        result: Result = player.equip(item_instance)
    elif command.subcommand == 'unequip':
        result: Result = player.unequip(item_instance)

    ui.print(result.msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- equipment')
    msg.append('- equipment equip [item]')
    msg.append('- equipment unequip[item]')
    msg.append('- equipment stats')

    return '\n'.join(msg)
