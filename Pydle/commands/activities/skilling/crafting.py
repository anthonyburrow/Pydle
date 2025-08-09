from ....lib.skilling.crafting import CRAFTABLES
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Craftable import Craftable
from ....util.player.Bank import Bank
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable


class CraftingActivity(Activity):

    name: str = 'craft'
    help_info: str = 'Begin crafting an item.'

    def __init__(self, *args):
        super().__init__(*args)

        self.craftable: ItemInstance | None = self.command.get_item_instance()
        self.required_items: list[ItemInstance] = [
            ITEM_PARSER.get_instance(item_name, quantity)
            for item_name, quantity in self.craftable.items_required.items()
        ]

        self.loot_table: LootTable = None

        self.description: str = 'crafting'

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- craft [item]')

        msg.append('')

        msg.append('Available items:')
        for item_id in CRAFTABLES:
            craftable: Craftable = ITEM_REGISTRY[item_id]
            msg.append(f'- {craftable}')

        return '\n'.join(msg)

    def setup_inherited(self) -> ActivitySetupResult:
        if self.craftable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        if not isinstance(self.craftable.base, Craftable):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.craftable} is not a valid craftable item.'
            )

        skill_level: int = self.player.get_level('crafting')
        if skill_level < self.craftable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.craftable.level} Crafting to craft a {self.craftable}.'
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
        ticks_per_action = self.craftable.ticks_per_action
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
            msg=f'Crafted a {self.craftable}!',
            items=items,
            xp={
                'crafting': self.craftable.xp,
            },
        )

    def finish_inherited(self):
        pass

    def _on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now crafting a {self.craftable}.'

    @property
    def standby_text(self) -> str:
        return 'Crafting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = (
            LootTable()
            .every(self.craftable)
        )

        # Add more stuff (pets, etc)
