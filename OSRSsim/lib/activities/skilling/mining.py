from ....util.structures.Activity import Activity
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Tool import Tool
from ...data.skilling.mining import Ore, ores


class MiningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.ore: Ore = None
        self.parse_args(*args[1:])

        self.description: str = 'mining'
        self.pickaxe: Tool = self.player.get_tool('pickaxe')

        self.loot_table: LootTable = None

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

        stat_level: int = self.player.get_level('mining')
        if stat_level < self.ore.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.ore.level} Mining to mine {self.ore.name}.'
            return status

        if self.pickaxe is None:
            status['success'] = False
            status['status_msg'] = \
                f'{self.player} does not have a pickaxe.'
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_use = self.pickaxe.ticks_per_use
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

        msg = f'Mined {items.list_concise()}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': items,
            'XP': {
                'mining': self.ore.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mining {self.ore.name}.'

    @property
    def standby_text(self) -> str:
        return 'Mining...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        mining_args = (
            self.player.get_level('mining'),
            self.pickaxe,
        )
        prob_success = self.ore.prob_success(*mining_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.ore.name, prob_success, self.ore.n_per_gather
        )

        # Add more stuff (pets, etc)
