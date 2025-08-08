from ....lib.skilling.herblore import MIXABLES
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Mixable import Mixable
from ....util.player.Bank import Bank
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable


class MixingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.mixable: ItemInstance | None = self.command.get_item_instance()
        self.required_items: list[ItemInstance] = [
            ITEM_PARSER.get_instance(item_name, quantity)
            for item_name, quantity in self.mixable.items_required.items()
        ]

        self.loot_table: LootTable = None

        self.description: str = 'mixing'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.mixable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        if not isinstance(self.mixable.base, Mixable):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.mixable} is not a valid mixable item.'
            )

        skill_level: int = self.player.get_level('herblore')
        if skill_level < self.mixable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.mixable.level} Herblore to mix a {self.mixable}.'
            )

        for item_instance in self.items_required:
            if self.player.has(item_instance):
                continue

            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have {item_instance.quantity}x {item_instance}.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        ticks_per_action = self.mixable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        for item_instance in self.items_required:
            if self.player.has(item_instance):
                continue

            return ActivityTickResult(
                msg=f'{self.player} ran out of {item_instance}.',
                exit=True,
            )

        for item_instance in self.items_required:
            self.player.remove(item_instance)

        items: Bank = self.loot_table.roll()

        return ActivityTickResult(
            msg=f'Mixed a {self.mixable}!',
            items=items,
            xp={
                'herblore': self.mixable.xp,
            },
        )

    def _on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mixing a {self.mixable}.'

    @property
    def standby_text(self) -> str:
        return 'Mixing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = (
            LootTable()
            .every(self.mixable)
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- mix [potion]')

    msg.append('')

    msg.append('Available potions:')
    for item_id in MIXABLES:
        mixable: Mixable = ITEM_REGISTRY[item_id]
        msg.append(f'- {mixable}')

    return '\n'.join(msg)
