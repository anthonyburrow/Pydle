from __future__ import annotations
from typing import TYPE_CHECKING, Type

from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.items.ItemInstance import ItemInstance
from ..util.items.ItemParser import ITEM_PARSER
from ..util.monsters.MonsterInstance import MonsterInstance
from ..util.monsters.MonsterParser import MONSTER_PARSER

if TYPE_CHECKING:
    from .CommandBase import CommandBase


CMD_EXIT: str = 'exit'


class Command:

    def __init__(self, raw: str):
        self.raw: str = raw

        self.command: str | None = None
        self.subcommand: str | None = None
        self.quantity: int = 1
        self.argument: str | None = None

        self.type: CommandType = CommandType.UNKNOWN
        self.action: Type[CommandBase] | None = None

        self._parse()
        self._set_info()

    def get_item_instance(self) -> ItemInstance | None:
        if not self.argument:
            return None
        return ITEM_PARSER.get_instance(self.argument, self.quantity)

    def get_monster_instance(self) -> MonsterInstance | None:
        if not self.argument:
            return None
        return MONSTER_PARSER.get_instance(self.argument)

    def _parse(self) -> None:
        tokens: list[str] = self.raw.strip().lower().split()

        if not tokens:
            return

        self.command = tokens.pop(0)
        self.action = COMMAND_REGISTRY.get(self.command)

        if not tokens:
            return

        subcommands: list[str] = self.action.subcommands if self.action else []
        if tokens[0] in subcommands:
            self.subcommand = tokens.pop(0)

        if not tokens:
            return

        try:
            self.quantity = int(tokens[0])
            tokens.pop(0)
        except ValueError:
            self.quantity = 1

        if not tokens:
            return

        self.argument = ' '.join(tokens)

    def _set_info(self):
        if self.command in COMMAND_REGISTRY.activities:
            self.type = CommandType.ACTIVITY
        elif self.command in COMMAND_REGISTRY.operations:
            self.type = CommandType.OPERATION
        elif self.command == CMD_EXIT:
            self.type = CommandType.EXIT
        else:
            self.type = CommandType.UNKNOWN
