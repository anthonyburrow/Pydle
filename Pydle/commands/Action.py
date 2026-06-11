from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from ..util.player.Player import Player
from ..util.structures.UserInterface import UserInterface

if TYPE_CHECKING:
    from .Command import Command


class Action(ABC):
    name: str
    aliases: list[str] = []
    subcommands: list[str] = []
    help_info: str = ''

    def __init__(self, player: Player, ui: UserInterface, command: Command):
        self.player: Player = player
        self.ui: UserInterface = ui
        self.command: Command = command

    @classmethod
    @abstractmethod
    def usage(cls) -> str:
        pass

    def print_usage(self) -> None:
        self.ui.print(self.usage(), multiline=True)
