from ...Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....lib.areas import AREAS
from ....util.items.Item import Item
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.player.Bank import Bank
from ....util.player.BankKey import BankKey
from ....util.player.ToolSlot import ToolSlot
from ....util.structures.Area import Area
from ....util.structures.LootTable import LootTable


class ForagingActivity(Activity):

    name: str = 'collect'
    help_info: str = 'Begin collecting resources from the area.'

    def __init__(self, *args):
        super().__init__(*args)

        self.area: Area = AREAS[self.player.area]
        self.secateurs: ItemInstance = self.player.get_tool(ToolSlot.SECATEURS)
        self.loot_table: LootTable = LootTable()
        self._xp_table: dict[BankKey, float] = {}

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- collect')

        return '\n'.join(msg)

    def setup(self) -> ActivitySetupResult:
        result: ActivitySetupResult = super().setup()
        if not result.success:
            return result

        if not self.area.collectables:
            return ActivitySetupResult(
                success=False,
                msg=f'There is nothing to be found in {self.area}.'
            )

        for collectable_name in self.area.collectables:
            item: Item = ITEM_PARSER.get_base(collectable_name)
            if self._has_level_requirement('foraging', item.level):
                break
        else:
            return ActivitySetupResult(
                success=False,
                msg=(
                    f'{self.player} does not have a high enough Foraging level'
                    f'to find any items in this area.'
                )
            )

        if not self.secateurs:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have any secateurs.'
            )

        return ActivitySetupResult(success=True)

    def begin(self) -> None:
        self._setup_loot_table()

        super().begin()

    def _process_tick(self) -> ActivityTickResult:
        ticks_per_use = self.secateurs.ticks_per_use
        if self.tick_count % ticks_per_use:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )
        
        return self._perform_action()

    def _perform_action(self) -> ActivityTickResult:
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

    def finish(self) -> None:
        super().finish()

    def _on_levelup(self):
        super()._on_levelup()

        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now collecting around {self.area}.'

    @property
    def standby_text(self) -> str:
        return 'Collecting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished foraging.'

    def _setup_loot_table(self):
        foraging_args = {
            'level': self.player.get_level('foraging'),
            'tool': self.secateurs,
        }

        empty_weight: float = 1.
        total_area_weight: int = sum(self.area.collectables.values())

        for collectable_name, area_weight in self.area.collectables.items():
            item_instance: ItemInstance = ITEM_PARSER.get_instance(collectable_name)
            item_instance.set_quantity(item_instance.n_per_gather)

            if not self._has_level_requirement('foraging', item_instance.level):
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
