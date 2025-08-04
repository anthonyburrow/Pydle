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
from ....util.items.skilling.Fish import Fish
from ....lib.skilling.fishing import FISH
from ....lib.areas import AREAS


class FishingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in FISH:
            self.fish: Fish = FISH[self.argument]
            self.fish_key: str = self.argument
        else:
            self.fish: Fish = None

        self.description: str = 'fishing'

        self.fishing_rod: Tool = self.player.get_tool('fishing rod')
        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.fish is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid fish was not given.'
            )

        skill_level: int = self.player.get_level('fishing')
        if skill_level < self.fish.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.fish.level} Fishing to fish {self.fish}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_fish(self.fish_key):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have {self.fish} anywhere.'
            )

        if not self.fishing_rod:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have a fishing rod.'
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
        fishing_args = (
            self.player.get_level('fishing'),
            self.fishing_rod,
        )
        prob_success = self.fish.prob_success(*fishing_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.fish.name, prob_success, self.fish.n_per_gather
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- fish [fish]')

    msg.append('')

    msg.append('Available fish:')
    for fish in FISH:
        name = str(fish).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
