import time
import keyboard
from enum import Enum

from . import Player, Controller
from .Skill import level_up_msg
from ..ticks import Ticks
from ..output import print_info
from ..commands import KEY_CANCEL
from ..misc import client_focused


class Status(Enum):
    STANDBY = 0
    ACTIVE = 1
    EXIT = 2


class Activity:

    def __init__(self, controller: Controller, *args):
        self.player: Player = controller.player
        self.client_ID = controller.client_ID

        self.tick_count: int = 0
        self.prev_status: int = Status.STANDBY

    def setup(self) -> dict:
        '''Check to see if requirements are met to perform activity.'''
        status = {
            'success': True,
            'msg': '',
        }

        # Setup for inherited classes
        status = self.setup_inherited(status)

        return status

    def begin_loop(self):
        '''Begin activity loop.'''
        print_info(self.startup_text)

        while True:
            if self._exit_command():
                self.finish()
                break

            # TODO: async timing, ditch all the time subtract
            start = time.time()

            process = self.update()

            if process['status'] == Status.EXIT:
                self.finish()
                break

            time_passed = time.time() - start
            time_to_wait = Ticks(1) - time_passed
            if time_to_wait > 0:
                time.sleep(time_to_wait)

    def update(self) -> dict:
        '''Processing during the tick.'''
        # Global update

        # Activity-specific update
        process: dict = self.update_inherited()

        if process['status'] != self.prev_status or self.tick_count == 0:
            self.prev_status = process['status']
            print_info(process['msg'])

        if 'items' in process:
            self.player.give(process['items'])

        if 'XP' in process:
            for skill, amount in process['XP'].items():
                XP_status = self.player.add_XP(skill, amount)

                if XP_status['leveled_up']:
                    print_info(level_up_msg(self.player, skill))
                    self.reset_on_levelup()

        # End of tick
        if process['status'] == Status.ACTIVE:
            self.player.save()

        self.tick_count += 1

        return process

    def finish(self) -> str:
        print_info(self.finish_text)

        msg = f'{self.player} is returning from {self.description}...'
        print_info(msg)

        self.finish_inherited()

        time.sleep(Ticks(4))

        return ''

    def _exit_command(self) -> bool:
        return keyboard.is_pressed(KEY_CANCEL) and client_focused(self.client_ID)
