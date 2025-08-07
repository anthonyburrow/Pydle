from enum import Enum, auto

from .items.ItemInstance import ItemInstance
from .items.ItemParser import ITEM_PARSER
from .monsters.MonsterInstance import MonsterInstance
from .monsters.MonsterParser import MONSTER_PARSER
from ..commands.command_map import map_activity, map_operations, alias_to_command


class CommandType(Enum):
    UNKNOWN = auto()
    OPERATION = auto()
    ACTIVITY = auto()
    EXIT = auto()


SUBCOMMANDS: dict[str, set[str]] = {
    'area': {'list'},
    'equipment': {'equip', 'unequip', 'stats'},
    'tools': {'equip', 'unequip'},
    'testing': {'skilling'},
}

CMD_EXIT: str = 'exit'


class Command:

    def __init__(self, raw: str):
        self.raw: str = raw

        self.command: str = None
        self.subcommand: str | None = None
        self.quantity: int | None = None
        self.argument: str | None = None

        self.type: CommandType = None

        self._parse()
        self._get_command_info()

    def get_item_instance(self) -> ItemInstance | None:
        return ITEM_PARSER.get_instance(self.argument, self.quantity)

    def get_monster_instance(self) -> MonsterInstance | None:
        return MONSTER_PARSER.get_instance(self.argument)

    def _parse(self) -> None:
        tokens = self.raw.strip().lower().split()

        self.command = tokens.pop(0)
        self.command = alias_to_command(self.command)

        if not tokens:
            return

        if self.command in SUBCOMMANDS and tokens[0] in SUBCOMMANDS[self.command]:
            self.subcommand = tokens.pop(0)

        if not tokens:
            return

        try:
            self.quantity = int(tokens[0])
            tokens.pop(0)
        except ValueError:
            self.quantity = 1

        if tokens:
            return

        self.argument = ' '.join(tokens)

    def _get_command_info(self) -> None:
        if self.command in map_activity:
            self.type = CommandType.ACTIVITY
        elif self.command in map_operations:
            self.type = CommandType.OPERATION
        elif self.command == CMD_EXIT:
            self.type = CommandType.EXIT
        elif self.command:
            self.type = CommandType.UNKNOWN
