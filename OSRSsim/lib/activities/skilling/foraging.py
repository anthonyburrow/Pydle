from ....util.structures.Activity import Activity, Status
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Tool import Tool
from ...data.skilling.foraging import Herb, herbs


class ForagingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.herb: Herb = None
        self.parse_args(*args[1:])

        self.description: str = 'foraging'

        self.secateurs: Tool = self.player.get_tool('secateurs')
        self.loot_table: LootTable = None

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
            status['msg'] = \
                'A valid herb was not given.'
            return status

        skill_level: int = self.player.get_level('foraging')
        if skill_level < self.herb.level:
            status['success'] = False
            status['msg'] = \
                f'You must have Level {self.herb.level} Foraging to collect {self.herb.name_grimy}.'
            return status

        if self.secateurs is None:
            status['success'] = False
            status['msg'] = \
                f'{self.player} does not have any secateurs.'
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = self.secateurs.ticks_per_use
        if self.tick_count % ticks_per_use:
            return {
                'status': Status.STANDBY,
                'msg': self.standby_text,
            }

        items: Bank = self.loot_table.roll()
        if not items:
            return {
                'status': Status.STANDBY,
                'msg': self.standby_text,
            }

        msg = f'Collected {items.list_concise()}!'

        return {
            'status': Status.ACTIVE,
            'msg': msg,
            'items': items,
            'XP': {
                'foraging': self.herb.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now collecting {self.herb.name_grimy}.'

    @property
    def standby_text(self) -> str:
        return 'Collecting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        foraging_args = (
            self.player.get_level('foraging'),
            self.secateurs,
        )
        prob_success = self.herb.prob_success(*foraging_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.herb.name_grimy, prob_success, self.herb.n_per_gather
        )

        # Add more stuff (pets, etc)
