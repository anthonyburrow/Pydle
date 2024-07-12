import time

from . import Player
from ..ticks import seconds_per_tick
from ..output import print_output


class Activity:

    def __init__(self, player: Player, *args):
        self.player: Player = player
        self.tick_count: int = 0

    def setup(self) -> dict:
        '''Check to see if requirements are met to perform activity.'''
        status = {
            'success': True,
            'status_msg': '',
        }

        if self.player.is_busy:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} is busy.'
            return status

        # Setup for inherited classes
        status = self.setup_inherited(status)

        return status

    def begin_loop(self):
        '''Begin activity loop.'''
        print_output(self.startup_text)

        while True:
            # TODO: async timing, ditch all the time subtract
            start = time.time()
            self.update()
            time_passed = time.time() - start

            time_to_wait = seconds_per_tick - time_passed
            if time_to_wait > 0:
                time.sleep(time_to_wait)

    def update(self):
        '''Processing during the tick.'''
        msg = self.update_inherited()
        print_output(msg)

        self.tick_count += 1

    def finish(self) -> str:
        # Return message, add loot to user, etc
        print_output(self.finish_text)

        self.finish_inherited()

        return ''

    @property
    def startup_text(self) -> str:
        return 'STARTED ACTIVITY'

    @property
    def finish_text(self) -> str:
        return 'FINISHED ACTIVITY'
