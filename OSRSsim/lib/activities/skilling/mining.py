from ....util.structures.Activity import Activity
from ....util.probability import roll
from ....util.ticks import seconds_per_tick, Ticks


ores = {
    'iron': {
        'name': 'Iron ore',
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

    def __init__(self, *args):
        super().__init__(*args)
        self.parse_args(*args[1:])

        self.description = 'mining'
        self.ticks_per_action: int = 3

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            mine 'ore'
        '''
        try:
            self.ore: str = args[0]
        except IndexError:
            self.ore: str = ''

    def setup_inherited(self, status: dict) -> dict:
        if self.ore not in ores:
            status['success'] = False
            status['status_msg'] = \
                f'{self.ore} is not a valid ore.'
            return status

        # Check if player has a pickaxe
        pickaxe = self._get_user_pickaxe()
        if pickaxe is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have a pickaxe.'
            return status

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        if self.tick_count % self.ticks_per_action:
            return {
                'status': 'standby',
                'status_msg': self.standby_text,
            }

        prob_success = ores[self.ore]['prob_success']
        if not roll(prob_success):
            return {
                'status': 'standby',
                'status_msg': self.standby_text,
            }

        quantity = ores[self.ore]['n_per_ore']
        self.player.give({self.ore: quantity})

        msg = f'Mined {quantity}x {self.ore}!'
        return {
            'status': 'action',
            'status_msg': msg,
        }

    def finish_inherited(self):
        pass

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mining {self.ore}.'

    @property
    def standby_text(self) -> str:
        return 'Mining...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _get_user_pickaxe(self) -> str:
        # TEST
        self.player.give('Iron pickaxe')

        for pickaxe in reversed(pickaxes):
            if self.player.has(pickaxe):
                return pickaxe

        return None

    def _calc_max_ore(self) -> int:
        prob_success = ores[self.ore]['prob_success']
        n_per_ore = ores[self.ore]['n_per_ore']
        pickaxe = self._get_user_pickaxe()
        ticks_per_mine = pickaxes[pickaxe]['ticks_per_mine']
        max_trip_time = self.player.max_trip_time

        n_ore = max_trip_time * seconds_per_tick * prob_success / ticks_per_mine
        n_ore = int(n_ore) * n_per_ore

        return n_ore
