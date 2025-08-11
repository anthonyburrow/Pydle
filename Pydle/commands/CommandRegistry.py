from __future__ import annotations
from typing import Type, TYPE_CHECKING
import importlib
import pkgutil

from .CommandType import CommandType
from . import activities, operations


if TYPE_CHECKING:
    from .Activity import Activity
    from .CommandBase import CommandBase
    from .Operation import Operation


CMD_EXIT: str = 'exit'


class CommandRegistry:

    def __init__(self):
        self.activities: dict[str, Type[Activity]] = {}
        self.operations: dict[str, Type[Operation]] = {}

        self.aliases: dict[str, str] = {}

    def load_commands(self) -> None:
        for package in (activities, operations):
            for _, name, _ in pkgutil.walk_packages(package.__path__, f'{package.__name__}.'):
                importlib.import_module(name)

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

    def get_type(self, name: str) -> CommandType:
        if name in self.aliases:
            name = self.aliases[name]
            print(name)

        if name in self.activities:
            return CommandType.ACTIVITY
        elif name in self.operations:
            return CommandType.OPERATION
        elif name == CMD_EXIT:
            return CommandType.EXIT
        else:
            return CommandType.UNKNOWN


COMMAND_REGISTRY = CommandRegistry()
