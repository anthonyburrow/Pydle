import time
import keyboard

from . import Player, Controller
from .Stat import Stat, level_up_msg
from ..ticks import Ticks
from ..output import print_output
from ..commands import KEY_CANCEL
from ..misc import client_focused


class Activity:

    def __init__(self, controller: Controller, *args):
        self.player: Player = controller.player
        self.client_ID = controller.client_ID

        self.tick_count: int = 0
        self.in_standby: bool = True

    def setup(self) -> dict:
        '''Check to see if requirements are met to perform activity.'''
        status = {
            'success': True,
            'status_msg': '',
        }

        # Setup for inherited classes
        status = self.setup_inherited(status)

        return status

    def begin_loop(self):
        '''Begin activity loop.'''
        print_output(self.startup_text)

        while True:
            if keyboard.is_pressed(KEY_CANCEL) and client_focused(self.client_ID):
                self.finish()

                msg = f'{self.player} is returning from {self.description}...'
                print_output(msg)
                time.sleep(Ticks(4))
                break

            # TODO: async timing, ditch all the time subtract
            start = time.time()
            self.update()
            time_passed = time.time() - start

            time_to_wait = Ticks(1) - time_passed
            if time_to_wait > 0:
                time.sleep(time_to_wait)

    def update(self):
        '''Processing during the tick.'''
        # Global update

        # Activity-specific update
        process: dict = self.update_inherited()

        if process['in_standby'] != self.in_standby or self.tick_count == 0:
            self.in_standby = process['in_standby']
            print_output(process['msg'])

        if 'items' in process:
            self.player.give(process['items'])

        if 'XP' in process:
            for stat, amount in process['XP'].items():
                XP_status = self.player.add_XP(stat, amount)

                if XP_status['leveled_up']:
                    print_output(level_up_msg(self.player, stat))

        # End of tick
        if not process['in_standby']:
            self.player.save()

        self.tick_count += 1

    def finish(self) -> str:
        # Return message, add loot to user, etc
        print_output(self.finish_text)

        self.finish_inherited()

        return ''
