from __future__ import annotations
from dataclasses import dataclass

from .Action import Action
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.items.ItemInstance import ItemInstance
from ..util.items.ItemParser import ITEM_PARSER
from ..util.monsters.MonsterInstance import MonsterInstance
from ..util.monsters.MonsterParser import MONSTER_PARSER


class InvalidCommandError(ValueError):
    pass


class EmptyCommandError(InvalidCommandError):
    pass


@dataclass(slots=True)
class Command:
    command: str
    subcommand: str | None
    quantity: int
    argument: str | None
    type: CommandType
    action: type[Action]

    def get_item_instance(self) -> ItemInstance | None:
        if not self.argument:
            return None

        return ITEM_PARSER.get_instance(self.argument, self.quantity)

    def get_monster_instance(self) -> MonsterInstance | None:
        if not self.argument:
            return None
        return MONSTER_PARSER.get_instance(self.argument)

    @staticmethod
    def get_action(command_name: str) -> type[Action]:
        try:
            return COMMAND_REGISTRY.get_action(command_name)
        except KeyError as exc:
            raise InvalidCommandError() from exc

    @classmethod
    def parse(cls, raw: str) -> Command:
        tokens: list[str] = raw.strip().lower().split()

        if not tokens:
            raise EmptyCommandError()

        command: str = tokens.pop(0)
        command_action: type[Action] = cls.get_action(command)
        command_type: CommandType = COMMAND_REGISTRY.get_type(command)

        subcommand: str | None = None
        quantity: int = 1
        argument: str | None = None

        subcommands: list[str] = command_action.subcommands
        if tokens and tokens[0] in subcommands:
            subcommand = tokens.pop(0)

        if tokens:
            try:
                quantity = int(tokens[0])
                tokens.pop(0)
            except ValueError:
                quantity = 1

        if tokens:
            argument = ' '.join(tokens)

        return cls(
            command=command,
            subcommand=subcommand,
            quantity=quantity,
            argument=argument,
            type=command_type,
            action=command_action,
        )

    def __bool__(self) -> bool:
        return bool(self.command)
