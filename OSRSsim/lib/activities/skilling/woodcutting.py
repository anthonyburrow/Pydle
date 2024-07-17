from ....util.structures.Activity import Activity
from ....util.probability import roll
from ...data.skilling.woodcutting import Log, logs, axes


class WoodcuttingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)
        self.parse_args(*args[1:])

        self.description = 'woodcutting'

        self.axe = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            chop 'log'
        '''
        try:
            self.log: Log = logs[args[0]]
        except (IndexError, KeyError):
            self.log: Log = None

    def setup_inherited(self, status: dict) -> dict:
        if self.log is None:
            status['success'] = False
            status['status_msg'] = \
                'A valid log was not given.'
            return status

        if self.player.get_level('woodcutting') < self.log.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.log.level} Woodcutting to chop {self.log.name}.'
            return status

        self.axe = self._get_user_axe()
        if self.axe is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have an axe.'
            return status

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = axes[self.axe]['ticks_per_use']
        if self.tick_count % ticks_per_use:
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        woodcutting_args = (
            self.player.get_level('woodcutting'),
            axes[self.axe]['power'],
            axes[self.axe]['level'],
        )
        prob_success = self.log.prob_success(*woodcutting_args)
        if not roll(prob_success):
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        quantity = self.log.n_per_log

        msg = f'Chopped {quantity}x {self.log.name}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': {
                self.log.name: quantity,
            },
            'XP': {
                'woodcutting': self.log.XP,
            },
        }

    def finish_inherited(self):
        pass

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now chopping {self.log.name}.'

    @property
    def standby_text(self) -> str:
        return 'Chopping...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _get_user_axe(self) -> str:
        for axe in reversed(axes):
            if self.player.has(axe):
                return axe

        return None
