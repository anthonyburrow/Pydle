from abc import ABC, abstractmethod

from .Command import Command
from ..util.structures.UserInterface import UserInterface
from ..util.player.Player import Player


class CommandBase(ABC):
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
    def usage(self) -> str:
        pass

    def print_usage(self) -> None:
        self.ui.print(self.usage(), multiline=True)
