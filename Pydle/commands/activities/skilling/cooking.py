from ....lib.skilling.cooking import COOKABLES
from ....lib.skilling.woodcutting import LOGS
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Cookable import Cookable
from ....util.player.Bank import Bank
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable


fire_effect = 'cooking fire'


class CookingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.cookable: ItemInstance | None = self.command.get_item_instance()
        self.required_items: list[ItemInstance] = [
            ITEM_PARSER.get_instance(item_name, quantity)
            for item_name, quantity in self.cookable.items_required.items()
        ]

        self.loot_table: LootTable = None

        self.description: str = 'cooking'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.cookable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        if not isinstance(self.cookable.base, Cookable):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.cookable} is not a valid cookable item.'
            )

        skill_level: int = self.player.get_level('cooking')
        if skill_level < self.cookable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.cookable.level} Cooking to cook {self.cookable}.'
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
        ticks_per_action = self.cookable.ticks_per_action
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

        if not items:
            return ActivityTickResult(
                msg=f'Burned {self.cookable}...',
                xp={
                    'cooking': self.cookable.xp * 0.5,
                },
            )

        return ActivityTickResult(
            msg=f'Cooked {self.cookable}!',
            items=items,
            xp={
                'cooking': self.cookable.xp,
            },
        )

    def finish_inherited(self):
        pass

    def _on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now cooking {self.cookable}.'

    @property
    def standby_text(self) -> str:
        return 'Cooking...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        cooking_args = {
            'level': self.player.get_level('cooking'),
        }
        prob_success = self.cookable.prob_success(**cooking_args)

        self.loot_table = (
            LootTable()
            .tertiary(self.cookable, prob_success)
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- cook [food]')

    msg.append('')

    msg.append('Available foods:')
    for item_id in COOKABLES:
        cookable: Cookable = ITEM_REGISTRY[item_id]
        msg.append(f'- {cookable}')

    return '\n'.join(msg)
