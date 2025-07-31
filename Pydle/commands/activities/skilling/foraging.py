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
from ....lib.skilling.foraging import Collectable, COLLECTABLES
from ....lib.areas import AREAS


class ForagingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.area: Area = AREAS[self.player.area]

        self.description: str = 'foraging'

        self.secateurs: Tool = self.player.get_tool('secateurs')
        self.loot_table: LootTable = None

        self._xp_table: dict = {}

    def setup_inherited(self) -> ActivitySetupResult:
        skill_level: int = self.player.get_level('foraging')

        if not self.area.collectables:
            return ActivitySetupResult(
                success=False,
                msg=f'There is nothing to be found in {area}.'
            )

        for collectable_key in self.area.collectables:
            collectable: Collectable = COLLECTABLES[collectable_key]
            if skill_level >= collectable.level:
                break
        else:
            return ActivitySetupResult(
                success=False,
                msg=(
                    f'{self.player} does not have a high enough Foraging level'
                    f'to find items in this area.'
                )
            )

        if not self.secateurs:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have any secateurs.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        ticks_per_use = self.secateurs.ticks_per_use
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

        # Loop needed in case of non-collectables (e.g. pets) in loot
        xp: float = 0
        for item in items:
            xp += self._xp_table.get(item, 0.)

        return ActivityTickResult(
            msg=f'Collected {items.list_concise()}!',
            items=items,
            xp={
                'foraging': xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now collecting around {self.area}.'

    @property
    def standby_text(self) -> str:
        return 'Collecting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        foraging_args = {
            'level': self.player.get_level('foraging'),
            'tool': self.secateurs,
        }

        self.loot_table = LootTable()

        empty_weight: float = 1.
        total_area_weight: int = sum(self.area.collectables.values())

        for collectable_key, area_weight in self.area.collectables.items():
            collectable: Collectable = COLLECTABLES[collectable_key]

            if self.player.get_level('foraging') < collectable.level:
                continue

            prob_success = collectable.prob_success(**foraging_args)
            adjusted_weight = prob_success * (area_weight / total_area_weight)
            self.loot_table.add(
                item=collectable.name,
                quantity=collectable.n_per_gather,
                weight=adjusted_weight,
            )

            empty_weight -= adjusted_weight

            self._xp_table[collectable.name] = collectable.xp

        empty_weight = max(0., empty_weight)
        self.loot_table.add_empty(weight=empty_weight)

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- collect')

    return '\n'.join(msg)
