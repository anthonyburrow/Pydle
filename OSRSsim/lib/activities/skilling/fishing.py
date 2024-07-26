from ....util.structures.Activity import Activity
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Tool import Tool
from ...data.skilling.fishing import Fish, fish


class FishingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.fish: Fish = None
        self.parse_args(*args[1:])

        self.description: str = 'fishing'

        self.fishing_rod: Tool = self.player.get_tool('fishing rod')
        self.loot_table: LootTable = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            fish 'fish'
        '''
        try:
            self.fish: Fish = fish[args[0]]
        except (IndexError, KeyError):
            self.fish: Fish = None

    def setup_inherited(self, status: dict) -> dict:
        if self.fish is None:
            status['success'] = False
            status['status_msg'] = \
                'A valid fish was not given.'
            return status

        skill_level: int = self.player.get_level('fishing')
        if skill_level < self.fish.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.fish.level} Fishing to fish {self.fish.name_cooked}.'
            return status

        if self.fishing_rod is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have a fishing rod.'
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = self.fishing_rod.ticks_per_use
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

        msg = f'Collected {items.list_concise()}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': items,
            'XP': {
                'fishing': self.fish.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now fishing {self.fish.name_cooked}.'

    @property
    def standby_text(self) -> str:
        return 'Fishing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        fishing_args = (
            self.player.get_level('fishing'),
            self.fishing_rod,
        )
        prob_success = self.fish.prob_success(*fishing_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.fish.name_raw, prob_success, self.fish.n_per_gather
        )

        # Add more stuff (pets, etc)
