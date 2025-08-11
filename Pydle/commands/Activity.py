from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from inspect import isabstract

from .CommandBase import CommandBase
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.colors import color, color_theme
from ..util.player.Bank import Bank
from ..util.player.Skill import Skill


class ActivityMsgType(Enum):
    WAITING = 0
    RESULT = 1


@dataclass
class ActivitySetupResult:
    success: bool = True
    msg: str = ''


@dataclass
class ActivityTickResult:
    msg: str = ''
    msg_type: ActivityMsgType = ActivityMsgType.RESULT
    items: Bank | None = None
    xp: dict | None = None


class Activity(CommandBase, ABC):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if not isabstract(cls):
            COMMAND_REGISTRY.register(cls, CommandType.ACTIVITY)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tick_count: int = 1
        self.is_active: bool = False
        self._previous_msg_type = ActivityMsgType.RESULT

    def setup(self) -> ActivitySetupResult:
        '''Check to see if requirements are met to perform activity.'''
        return ActivitySetupResult(success=True)

    def begin(self) -> None:
        self.is_active = True
        self.ui.start_keyboard_listener()

        self.ui.print(self.startup_text)

    @abstractmethod
    def _process_tick(self) -> ActivityTickResult:
        pass

    def update(self) -> None:
        result_tick: ActivityTickResult = self._process_tick()

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
        if not self.tick_count % 50:
            self.player.save()

        result_recheck: ActivitySetupResult = self._recheck()
        if not result_recheck.success or not self.ui.activity_running:
            self.is_active = False

        self.tick_count += 1

    def _recheck(self) -> ActivitySetupResult:
        return ActivitySetupResult(success=True)

    def finish(self) -> None:
        self.ui.print(self.finish_text)

        self.ui.stop_keyboard_listener()

    @property
    @abstractmethod
    def startup_text(self) -> str:
        return ''

    @property
    @abstractmethod
    def standby_text(self) -> str:
        return ''

    @property
    @abstractmethod
    def finish_text(self) -> str:
        return ''

    def _has_level_requirement(self, skill_key: str, level_req: int) -> bool:
        return self.player.get_level(skill_key) >= level_req

    def _on_levelup(self) -> None:
        pass

    def _level_up_msg(self, skill_key: str) -> None:
        skill: Skill = self.player.get_skill(skill_key)

        level: str = str(skill.level)
        if skill.level >= 99:
            level = color(level, color_theme['skill_lvl99'])

        self.ui.print(f"{self.player}'s {skill} level has increased to Level {level}!")
