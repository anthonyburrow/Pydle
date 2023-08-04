import time
import asyncio

from .. import Player
from ..ticks import seconds_per_tick
from ..io import print_output


class Activity:

    def __init__(self, player: Player, *args, **kwargs):
        self.player = player
        self.ticks = 0

    def setup(self) -> dict:
        # Check to see if user may go on trip, calculate things for startup
        output = {'able': True, 'out_text': ''}
        return output

    async def begin(self):
        msg = ''

        while True:
            start = time.time()
            msg = await self.simulate_tick()
            self.ticks += 1
            time_passed = time.time() - start

            time_to_wait = seconds_per_tick - time_passed
            if time_to_wait > 0:
                await asyncio.sleep(time_to_wait)

            print_output(msg)

    async def simulate_tick(self):
        pass

    def update(self) -> str:
        # Wait the duration
        pass

    def finish(self) -> str:
        # Return message, add loot to user, etc
        return ''
