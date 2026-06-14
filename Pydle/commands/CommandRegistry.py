from __future__ import annotations

import importlib
import pkgutil
from typing import TYPE_CHECKING

from . import activities, operations
from .CommandType import CommandType

if TYPE_CHECKING:
    from .Action import Action


CMD_EXIT: str = 'exit'


class CommandRegistry:
    def __init__(self):
        self.activities: dict[str, type[Action]] = {}
        self.operations: dict[str, type[Action]] = {}

        self.aliases: dict[str, str] = {}

    def load_commands(self) -> None:
        for package in (activities, operations):
            for _, name, _ in pkgutil.walk_packages(
                package.__path__, f'{package.__name__}.'
            ):
                importlib.import_module(name)

    def register(
        self, command_action: type[Action], command_type: CommandType
    ) -> None:
        if command_type == CommandType.ACTIVITY:
            self.activities[command_action.name] = command_action
        elif command_type == CommandType.OPERATION:
            self.operations[command_action.name] = command_action

        for alias in command_action.aliases:
            if alias in self.activities or alias in self.operations:
                raise KeyError(
                    f"Attempted alias creation for {command_action.name} already a command name: '{alias}'"
                )
            if alias in self.aliases:
                raise KeyError(
                    f"Attempted alias creation for {command_action.name} already created: '{alias}'"
                )
            self.aliases[alias] = command_action.name

    def get_action(self, name: str) -> type[Action]:
        if name in self.aliases:
            name = self.aliases[name]

        if name in self.activities:
            return self.activities[name]
        elif name in self.operations:
            return self.operations[name]

        raise KeyError(f"Unknown command: '{name}'")

    def get_type(self, name: str) -> CommandType:
        if name in self.aliases:
            name = self.aliases[name]

        if name in self.activities:
            return CommandType.ACTIVITY
        elif name in self.operations:
            return CommandType.OPERATION

        raise KeyError(f"Unknown command: '{name}'")


COMMAND_REGISTRY = CommandRegistry()
