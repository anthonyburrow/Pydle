from ....lib.areas import AREAS
from ....util.items.Item import Item, ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.player.Bank import Bank, BankKey
from ....util.player.Tools import ToolSlot
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Area import Area
from ....util.structures.LootTable import LootTable


class ForagingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.area: Area = AREAS[self.player.area]

        self.description: str = 'foraging'

        self.secateurs: ItemInstance = self.player.get_tool(ToolSlot.SECATEURS)
        self.loot_table: LootTable = None

        self._xp_table: dict[BankKey, float] = {}

    def setup_inherited(self) -> ActivitySetupResult:
        if not self.area.collectables:
            return ActivitySetupResult(
                success=False,
                msg=f'There is nothing to be found in {self.area}.'
            )

        skill_level: int = self.player.get_level('foraging')

        for collectable_name in self.area.collectables:
            item: Item = ITEM_PARSER.get_base(collectable_name)
            if skill_level >= item.level:
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
        for bank_key in items:
            xp += self._xp_table.get(bank_key, 0.)

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

        for collectable_name, area_weight in self.area.collectables.items():
            item_instance: ItemInstance = ITEM_PARSER.get_instance(collectable_name)

            if self.player.get_level('foraging') < item_instance.level:
                continue

            prob_success = item_instance.prob_success(**foraging_args)
            adjusted_weight = prob_success * (area_weight / total_area_weight)
            self.loot_table.add(
                item_instance=item_instance,
                weight=adjusted_weight,
            )

            empty_weight -= adjusted_weight

            self._xp_table[item_instance.get_key()] = item_instance.xp

        empty_weight = max(0., empty_weight)
        self.loot_table.add_empty(weight=empty_weight)

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- collect')

    return '\n'.join(msg)
