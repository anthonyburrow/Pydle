# import asyncio
import numpy as np

from ....util import Activity, Ticks, roll
from ...constants import sec_per_tick


ores = {
    'Iron ore': {
        'xp': 35,
        'prob_success': 0.5,
        'n_per_ore': 1
    }
}

pickaxes = {
    'Iron pickaxe': {
        'ticks_per_mine': 3
    }
}


class MiningActivity(Activity):

    def __init__(self, ore: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ore = ore

        self.ticks_per_action = 3
        self.idle_msg = f'Mining...'

    def setup(self) -> dict:
        output = {'able': False}

        pickaxe = self._get_user_pickaxe()
        if pickaxe is None:
            msg = f'{self.player.name} does not have {pickaxe}.'
            output['out_text'] = msg
            return output

        output['able'] = True
        output['out_text'] = self._startup_text()

        return output

    async def simulate_tick(self) -> str:
        if self.ticks % self.ticks_per_action:
            return self.idle_msg

        prob_success = ores[self.ore]['prob_success']
        if not roll(prob_success):
            return self.idle_msg

        quantity = ores[self.ore]['n_per_ore']
        self.player.bank.add({self.ore: quantity})

        return f'Mined {quantity}x {self.ore}! ({self.player.bank.quantity(self.ore)})'

    def finish(self) -> str:
        msg = (
            f'{self.player.name} finished mining.'
        )
        return msg

    def _startup_text(self) -> str:
        msg = (
            f'{self.player.name} is now mining {self.ore}. '
        )
        return msg

    def _get_user_pickaxe(self) -> str:
        for pickaxe in reversed(pickaxes):
            if self.player.bank.contains(pickaxe):
                return pickaxe

        return None

    def _calc_max_ore(self) -> int:
        prob_success = ores[self.ore]['prob_success']
        n_per_ore = ores[self.ore]['n_per_ore']
        pickaxe = self._get_user_pickaxe()
        ticks_per_mine = pickaxes[pickaxe]['ticks_per_mine']
        max_trip_time = self.player.max_trip_time

        n_ore = max_trip_time * sec_per_tick * prob_success / ticks_per_mine
        n_ore = int(n_ore) * n_per_ore

        return n_ore
