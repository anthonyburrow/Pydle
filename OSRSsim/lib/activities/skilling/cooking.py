from ....util.structures.Activity import Activity
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ...data.skilling.cooking import Cookable, cookables


class CookingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.cookable: Cookable = None
        self.parse_args(*args[1:])

        self.description: str = 'cooking'

        self.loot_table: LootTable = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            cook 'food'
        '''
        try:
            self.cookable: Cookable = cookables[args[0]]
        except (IndexError, KeyError):
            self.cookable: Cookable = None

    def setup_inherited(self, status: dict) -> dict:
        if self.cookable is None:
            status['success'] = False
            status['status_msg'] = \
                'A valid item was not given.'
            return status

        skill_level: int = self.player.get_level('cooking')
        if skill_level < self.cookable.level:
            status['success'] = False
            status['status_msg'] = \
                f'You must have Level {self.cookable.level} Cooking to cook {self.cookable.name}.'
            return status

        # Logs?

        check_items = self.has_items(self.cookable.items_required)
        if not check_items['success']:
            item = check_items['item']
            quantity = check_items['quantity']
            msg = f'{self.player} does not have {quantity}x {item}.'

            status['success'] = False
            status['status_msg'] = msg

            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        ticks_per_action = self.cookable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return {
                'in_standby': True,
                'msg': self.standby_text,
            }

        check_items = self.has_items(self.cookable.items_required)
        if not check_items['success']:
            item = check_items['item']
            quantity = check_items['quantity']
            msg = f'{self.player} does not have {quantity}x {item}.'
            return {
                'success': False,
                'in_standby': False,
                'msg': msg,
            }

        for item, quantity in self.cookable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()
        if not items:
            msg = f'Burned {self.cookable.name}...'
            return {
                'in_standby': False,
                'msg': msg,
            }

        msg = f'Cooked {self.cookable.name}!'

        return {
            'in_standby': False,
            'msg': msg,
            'items': items,
            'XP': {
                'cooking': self.cookable.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now cooking {self.cookable.name}.'

    @property
    def standby_text(self) -> str:
        return 'Cooking...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        cooking_args = (
            self.player.get_level('cooking'),
        )
        prob_success = self.cookable.prob_success(*cooking_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.cookable.name, prob_success, 1
        )

        # Add more stuff (pets, etc)

    def has_items(self, items: dict) -> dict:
        for item, quantity in items.items():
            if not self.player.has(item, quantity):
                return {
                    'success': False,
                    'item': item,
                    'quantity': quantity,
                }

        return {
            'success': True,
        }
