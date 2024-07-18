from ....util.structures.Activity import Activity
from ....util.probability import roll
from ...data.skilling.mining import Ore, ores, pickaxes


class MiningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)
        self.parse_args(*args[1:])

        self.description = 'mining'

        self.pickaxe = None

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

        if self.player.get_level('mining') < self.ore.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.ore.level} Mining to mine {self.ore.name}.'
            return status

        self.pickaxe = self._get_user_pickaxe()
        if self.pickaxe is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have a pickaxe.'
            return status

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = pickaxes[self.pickaxe]['ticks_per_use']
        if self.tick_count % ticks_per_use:
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        mining_args = (
            self.player.get_level('mining'),
            pickaxes[self.pickaxe]['power'],
            pickaxes[self.pickaxe]['level'],
        )
        prob_success = self.ore.prob_success(*mining_args)
        if not roll(prob_success):
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        quantity = self.ore.n_per_gather

        msg = f'Mined {quantity}x {self.ore.name}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': {
                self.ore.name: quantity,
            },
            'XP': {
                'mining': self.ore.XP,
            },
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
