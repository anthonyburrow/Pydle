from ....lib.areas import AREAS
from ....lib.skilling.mining import ORES
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Ore import Ore
from ....util.player.Bank import Bank
from ....util.player.ToolSlot import ToolSlot
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Area import Area
from ....util.structures.LootTable import LootTable


class MiningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.ore: ItemInstance | None = self.command.get_item_instance()
        self.ore.set_quantity(self.ore.n_per_gather)

        self.pickaxe: ItemInstance | None = self.player.get_tool(ToolSlot.PICKAXE)
        self.loot_table: LootTable = None

        self.description: str = 'mining'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.ore is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid ore was not given.'
            )

        if not isinstance(self.ore.base, Ore):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.ore} is not a valid ore.'
            )

        skill_level: int = self.player.get_level('mining')
        if skill_level < self.ore.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.ore.level} Mining to mine {self.ore}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_ore(self.ore):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have {self.ore} anywhere.'
            )

        if not self.pickaxe:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have a pickaxe equipped.'
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

    def _on_levelup(self):
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

        self.loot_table = (
            LootTable()
            .tertiary(self.ore, prob_success)
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- mine [ore]')

    msg.append('')

    msg.append('Available ores:')
    for item_id in ORES:
        ore: Ore = ITEM_REGISTRY[item_id]
        msg.append(f'- {ore}')

    return '\n'.join(msg)
