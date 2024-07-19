from ....util.structures.Activity import Activity
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ...data.skilling.woodcutting import Log, logs, axes


class WoodcuttingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.log: Log = None
        self.parse_args(*args[1:])

        self.description: str = 'woodcutting'

        self.axe: str = None
        self.loot_table: LootTable = None

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

        stat_level: int = self.player.get_level('woodcutting')
        if stat_level < self.log.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.log.level} Woodcutting to chop {self.log.name}.'
            return status

        self.axe: str = self.player.get_tool('axe')
        if self.axe is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have an axe.'
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = axes[self.axe]['ticks_per_use']
        if self.tick_count % ticks_per_use:
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        items: Bank = self.loot_table.roll()
        if not items:
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        msg = f'Chopped {items.list_concise()}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': items,
            'XP': {
                'woodcutting': self.log.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now chopping {self.log.name}.'

    @property
    def standby_text(self) -> str:
        return 'Chopping...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        woodcutting_args = (
            self.player.get_level('woodcutting'),
            axes[self.axe]['power'],
            axes[self.axe]['level'],
        )
        prob_success = self.log.prob_success(*woodcutting_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.log.name, prob_success, self.log.n_per_gather
        )

        # Add more stuff (pets, etc)
