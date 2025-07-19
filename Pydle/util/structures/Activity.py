from enum import Enum
from dataclasses import dataclass
import keyboard

from . import Player
from .Bank import Bank
from .Skill import level_up_msg
from ..output import print_info
from ..misc import client_focused
from ..commands import KEY_CANCEL


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

    def __init__(self, player: Player, client_ID: int, *args):
        self.player: Player = player
        self.client_ID: int = client_ID

        self.argument = ' '.join(args)

        self.tick_count: int = 0
        self.is_active: bool = False
        self._previous_msg_type = ActivityMsgType.RESULT

    def setup(self) -> dict:
        '''Check to see if requirements are met to perform activity.'''
        result_setup = self.setup_inherited()

        return result_setup

    def begin(self) -> None:
        self.is_active = True
        print_info(self.startup_text)

    def update(self) -> None:
        '''Processing during the tick.'''
        result_tick: ActivityTickResult = self.update_inherited()

        if (
            result_tick.msg_type == ActivityMsgType.RESULT or
            self._previous_msg_type != ActivityMsgType.WAITING
        ):
            print_info(result_tick.msg)
        self._previous_msg_type = result_tick.msg_type

        if result_tick.items is not None:
            self.player.give(result_tick.items)

        if result_tick.xp is not None:
            for skill, amount in result_tick.xp.items():
                XP_status = self.player.add_XP(skill, amount)

                if XP_status['leveled_up']:
                    print_info(level_up_msg(self.player, skill))
                    self.reset_on_levelup()

        # Global updates
        self.player.update_effects()

        # End of tick
        if result_tick.exit or self._check_input_standby():
            self.is_active = False

        if not result_tick.exit and not self.tick_count % 50:
            self.player.save()

        self.tick_count += 1

    def finish(self) -> None:
        print_info(self.finish_text)

        print_info(f'{self.player} is returning from {self.description}...')

        self.finish_inherited()

    def _check_input_standby(self) -> bool:
        return (
            keyboard.is_pressed(KEY_CANCEL) and
            client_focused(self.client_ID)
        )
