from ....util.structures.Activity import Activity
from ....util.probability import roll
from ....util.ticks import seconds_per_tick, Ticks


class Ore:

    def __init__(self, name: str, xp: int, prob_success: float,
                 n_per_ore : int=1):
        self.name = name
        self.xp = xp
        self.prob_success = prob_success
        self.n_per_ore = n_per_ore

ores = {
    'iron': Ore(
        name='Iron ore',
        xp=35,
        prob_success=0.5,
    ),
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
            self.ore: Ore = ores[args[0]]
        except (IndexError, KeyError):
            self.ore: Ore = None

    def setup_inherited(self, status: dict) -> dict:
        if self.ore is None:
            status['success'] = False
            status['status_msg'] = \
                'A valid ore was not given.'
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

        prob_success = self.ore.prob_success
        if not roll(prob_success):
            return {
                'status': 'standby',
                'status_msg': self.standby_text,
            }

        quantity = self.ore.n_per_ore
        self.player.give({self.ore.name: quantity})

        msg = f'Mined {quantity}x {self.ore.name}!'
        return {
            'status': 'action',
            'status_msg': msg,
        }

    def finish_inherited(self):
        pass

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mining {self.ore.name}.'

    @property
    def standby_text(self) -> str:
        return 'Mining...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _get_user_pickaxe(self) -> str:
        for pickaxe in reversed(pickaxes):
            if self.player.has(pickaxe):
                return pickaxe

        return None
