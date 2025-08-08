from dataclasses import dataclass
from enum import Enum

from .UserInterface import UserInterface
from ..Command import Command
from ..colors import color, color_theme
from ..player.Bank import Bank
from ..player.Player import Player
from ..player.Skill import level_up_msg


@dataclass
class ActivitySetupResult:
    success: bool = True
    msg: str = ''


class ActivityMsgType(Enum):
    WAITING = 0
    RESULT = 1


@dataclass
class ActivityTickResult:
    msg: str = ''
    msg_type: ActivityMsgType = ActivityMsgType.RESULT
    exit: bool = False
    #
    items: Bank = None
    xp: dict = None


class Activity:

    def __init__(self, player: Player, ui: UserInterface, command: Command):
        self.player: Player = player
        self.ui: UserInterface = ui
        self.command: Command = command

        self.tick_count: int = 0
        self.is_active: bool = False
        self._previous_msg_type = ActivityMsgType.RESULT

    def setup(self) -> dict:
        '''Check to see if requirements are met to perform activity.'''
        result_setup = self.setup_inherited()

        return result_setup

    def begin(self) -> None:
        self.is_active = True
        self.ui.start_keyboard_listener()

        self.ui.print(self.startup_text)

    def update(self) -> None:
        '''Processing during the tick.'''
        result_tick: ActivityTickResult = self.update_inherited()

        if (
            result_tick.msg_type == ActivityMsgType.RESULT or
            self._previous_msg_type != ActivityMsgType.WAITING
        ):
            self.ui.print(result_tick.msg)
        self._previous_msg_type = result_tick.msg_type

        if result_tick.items:
            self.player.give(result_tick.items)

        if result_tick.xp:
            leveled_up: bool = False
            for skill, amount in result_tick.xp.items():
                xp_status = self.player.add_xp(skill, amount)

                if xp_status['leveled_up']:
                    leveled_up = True
                    self._level_up_msg(skill)

            if leveled_up:
                self._on_levelup()

        # Global updates
        self.player.update_effects()

        # End of tick
        if result_tick.exit or not self.ui.activity_running:
            self.is_active = False

        if not result_tick.exit and not self.tick_count % 50:
            self.player.save()

        self.tick_count += 1

    def finish(self) -> None:
        self.ui.print(self.finish_text)
        self.ui.print(f'{self.player} is returning from {self.description}...')

        self.ui.stop_keyboard_listener()

        self.finish_inherited()

    def _on_levelup(self):
        self._level_up_msg()

    def _level_up_msg(self, skill_key: str) -> None:
        skill = self.player.get_skill(skill_key)

        level = skill.level
        if level >= 99:
            level = color(level, color_theme['skill_lvl99'])

        self.ui.print(f"{self.player}'s {skill} level has increased to Level {level}!")
