from ....util.structures.Activity import Activity
from ....util.probability import roll
from ...data.skilling.foraging import Herb, herbs, secateurs


class ForagingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)
        self.parse_args(*args[1:])

        self.description = 'foraging'

        self.secateurs = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            collect 'herb/item'
        '''
        try:
            self.herb: Herb = herbs[args[0]]
        except (IndexError, KeyError):
            self.herb: Herb = None

    def setup_inherited(self, status: dict) -> dict:
        if self.herb is None:
            status['success'] = False
            status['status_msg'] = \
                'A valid herb was not given.'
            return status

        if self.player.get_level('foraging') < self.herb.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.herb.level} Foraging to collect {self.herb.name_grimy}.'
            return status

        self.secateurs = self._get_user_secateurs()
        if self.secateurs is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have any secateurs.'
            return status

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = secateurs[self.secateurs]['ticks_per_use']
        if self.tick_count % ticks_per_use:
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        foraging_args = (
            self.player.get_level('foraging'),
            secateurs[self.secateurs]['power'],
            secateurs[self.secateurs]['level'],
        )
        prob_success = self.herb.prob_success(*foraging_args)
        if not roll(prob_success):
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        quantity = self.herb.n_per_gather

        msg = f'Collected {quantity}x {self.herb.name_grimy}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': {
                self.herb.name_grimy: quantity,
            },
            'XP': {
                'foraging': self.herb.XP,
            },
        }

    def finish_inherited(self):
        pass

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now collecting {self.herb.name_grimy}.'

    @property
    def standby_text(self) -> str:
        return 'Collecting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _get_user_secateurs(self) -> str:
        for secateur in reversed(secateurs):
            if self.player.has(secateur):
                return secateur

        return None
