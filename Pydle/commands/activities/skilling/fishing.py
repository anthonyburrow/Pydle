from ....util.ItemRegistry import ITEM_REGISTRY
from ....util.ItemParser import ITEM_PARSER
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Tools import ToolSlot
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Area import Area
from ....util.items.Item import ItemInstance
from ....util.items.skilling.Fish import Fish
from ....lib.skilling.fishing import FISH
from ....lib.areas import AREAS


class FishingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.fish: ItemInstance | None = ITEM_PARSER.get_instance(self.command)
        self.fish.set_quantity(self.fish.n_per_gather)

        self.fishing_rod: ItemInstance | None = self.player.get_tool(ToolSlot.FISHING_ROD)
        self.loot_table: LootTable = None

        self.description: str = 'fishing'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.fish is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        if not isinstance(self.fish, Fish):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.fish} is not a valid fish.'
            )

        skill_level: int = self.player.get_level('fishing')
        if skill_level < self.fish.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.fish.level} Fishing to fish {self.fish}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_fish(self.fish):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have {self.fish} anywhere.'
            )

        if not self.fishing_rod:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have a fishing rod equipped.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        ticks_per_use = self.fishing_rod.ticks_per_use
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
            msg=f'Fished {items.list_concise()}!',
            items=items,
            xp={
                'fishing': self.fish.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now fishing {self.fish}.'

    @property
    def standby_text(self) -> str:
        return 'Fishing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        fishing_args = {
            'level': self.player.get_level('fishing'),
            'tool': self.fishing_rod,
        }
        prob_success = self.fish.prob_success(**fishing_args)

        self.loot_table = (
            LootTable()
            .tertiary(self.fish, prob_success)
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- fish [fish]')

    msg.append('')

    msg.append('Available fish:')
    for item_id in FISH:
        fish: Fish = ITEM_REGISTRY[item_id]
        msg.append(f'- {fish}')

    return '\n'.join(msg)
