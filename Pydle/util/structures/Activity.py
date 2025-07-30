from enum import Enum
from dataclasses import dataclass
from pynput import keyboard

from .Player import Player
from .UserInterface import UserInterface
from .Bank import Bank
from .Skill import level_up_msg
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

    def __init__(self, player: Player, ui: UserInterface, *args):
        self.player: Player = player
        self.ui: UserInterface = ui

        self.argument: str = ' '.join(args)

        self.tick_count: int = 0
        self.is_active: bool = False
        self._previous_msg_type = ActivityMsgType.RESULT

        self.listener = keyboard.Listener(
            on_release=self.manual_cancel
        )
        self.listener.start()

    def setup(self) -> dict:
        '''Check to see if requirements are met to perform activity.'''
        result_setup = self.setup_inherited()

        return result_setup

    def begin(self) -> None:
        self.is_active = True
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
            for skill, amount in result_tick.xp.items():
                xp_status = self.player.add_xp(skill, amount)

                if xp_status['leveled_up']:
                    self.ui.print(level_up_msg(self.player, skill))
                    self.reset_on_levelup()

        # Global updates
        self.player.update_effects()

        # End of tick
        if result_tick.exit:
            self.is_active = False

        if not result_tick.exit and not self.tick_count % 50:
            self.player.save()

        self.tick_count += 1

    def finish(self) -> None:
        self.ui.print(self.finish_text)
        self.ui.print(f'{self.player} is returning from {self.description}...')

        self.listener.stop()

        self.finish_inherited()

    def manual_cancel(self, key):
        if not isinstance(key, keyboard.KeyCode):
            return

        if key.char == KEY_CANCEL and self.ui.is_focused():
            self.is_active = False
