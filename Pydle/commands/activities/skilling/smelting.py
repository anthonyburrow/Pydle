from ....util.ItemRegistry import ITEM_REGISTRY
from ....util.ItemParser import ITEM_PARSER
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.items.Item import ItemInstance
from ....util.items.skilling.Smeltable import Smeltable
from ....lib.skilling.smithing import SMELTABLES
from ....lib.skilling.woodcutting import LOGS


fire_effect = 'smithing fire'


class SmeltingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.smeltable: ItemInstance | None = \
            ITEM_PARSER.get_instance_by_command(self.command)
        self.required_items: list[ItemInstance] = [
            ITEM_PARSER.get_instance(item_name, quantity)
            for item_name, quantity in self.smeltable.items_required.items()
        ]

        self.loot_table: LootTable = None

        self.description: str = 'smelting'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.smeltable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        if not isinstance(self.smeltable.base, Smeltable):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.smeltable} is not a valid smeltable item.'
            )

        skill_level: int = self.player.get_level('smithing')
        if skill_level < self.smeltable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.smeltable.level} Smithing to smelt a {self.smeltable}.'
            )

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance = \
                    ITEM_PARSER.get_instance_by_id(item_id)
                if self.player.has(item_instance):
                    break
            else:
                return ActivitySetupResult(
                    success=False,
                    msg=f'{self.player} has no logs to make a fire.'
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
        ticks_per_action = self.smeltable.ticks_per_action
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

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance = \
                    ITEM_PARSER.get_instance_by_id(item_id)
                if self.player.has(item_instance):
                    self.player.remove(item_instance)
                    self.player.add_effect(fire_effect, item_instance.ticks_per_fire)
                    break
            else:
                return ActivityTickResult(
                    msg=f'{self.player} ran out of logs.',
                    exit=True,
                )

        for item_instance in self.items_required:
            self.player.remove(item_instance)

        items: Bank = self.loot_table.roll()

        return ActivityTickResult(
            msg=f'Smelted a {self.smeltable}!',
            items=items,
            xp={
                'smithing': self.smeltable.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now smelting a {self.smeltable}.'

    @property
    def standby_text(self) -> str:
        return 'Smelting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = (
            LootTable()
            .every(self.smeltable)
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- smelt [ore]')

    msg.append('')

    msg.append('Available ores:')
    for item_id in SMELTABLES:
        smeltable: Smeltable = ITEM_REGISTRY[item_id]
        msg.append(f'- {smeltable}')

    return '\n'.join(msg)
