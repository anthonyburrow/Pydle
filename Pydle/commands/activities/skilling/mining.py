from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Tool import Tool
from ....util.structures.Area import Area
from ....lib.skilling.mining import Ore, ORES
from ....lib.areas import AREAS


class MiningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in ORES:
            self.ore: Ore = ORES[self.argument]
            self.ore_key: str = self.argument
        else:
            self.ore: Ore = None

        self.description: str = 'mining'
        self.pickaxe: Tool = self.player.get_tool('pickaxe')

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.ore is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid ore was not given.'
            )

        skill_level: int = self.player.get_level('mining')
        if skill_level < self.ore.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.ore.level} Mining to mine {self.ore}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_ore(self.ore_key):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have {self.ore} anywhere.'
            )

        if self.pickaxe is None:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have a pickaxe.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        ticks_per_use = self.pickaxe.ticks_per_use
        if self.tick_count % ticks_per_use:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        items: Bank = self.loot_table.roll()
        if not items:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        return ActivityTickResult(
            msg=f'Mined {items.list_concise()}!',
            items=items,
            xp={
                'mining': self.ore.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mining {self.ore}.'

    @property
    def standby_text(self) -> str:
        return 'Mining...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        mining_args = {
            'level': self.player.get_level('mining'),
            'tool': self.pickaxe,
        }
        prob_success = self.ore.prob_success(**mining_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.ore.name, prob_success, self.ore.n_per_gather
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- mine [ore]')

    msg.append('')

    msg.append('Available ores:')
    for ore in ORES:
        name = str(ore).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
