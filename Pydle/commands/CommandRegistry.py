from __future__ import annotations
from typing import Type, TYPE_CHECKING

from .CommandType import CommandType


if TYPE_CHECKING:
    from .Activity import Activity
    from .CommandBase import CommandBase
    from .Operation import Operation


class CommandRegistry:

    def __init__(self):
        self.activities: dict[str, Type[Activity]] = {}
        self.operations: dict[str, Type[Operation]] = {}

        self.aliases: dict[str, str] = {}

    def register(self, command_cls: Type[CommandBase], command_type: CommandType) -> None:
        if command_type == CommandType.ACTIVITY:
            self.activities[command_cls.name] = command_cls
        elif command_type == CommandType.OPERATION:
            self.operations[command_cls.name] = command_cls

        for alias in command_cls.aliases:
            if alias in self.activities or alias in self.operations:
                raise KeyError(
                    f"Attempted alias creation for {command_cls.name} already a command name: '{alias}'"
                )
            if alias in self.aliases:
                raise KeyError(
                    f"Attempted alias creation for {command_cls.name} already created: '{alias}'"
                )
            self.aliases[alias] = command_cls.name

    def get(self, name: str) -> Type[CommandBase] | None:
        if name in self.aliases:
            name = self.aliases[name]

        if name in self.activities:
            return self.activities.get(name)

        if name in self.operations:
            return self.operations.get(name)


COMMAND_REGISTRY = CommandRegistry()
