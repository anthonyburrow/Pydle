from collections.abc import Callable

from ...util.items.ItemParser import ITEM_PARSER
from ...util.player.Bank import Bank
from ...util.player.Player import Player


class SetupManager:

    def __init__(self):
        self._setups: dict[str, Callable[[Player], None]] = {
            'skilling': self._setup_skilling,
        }

    def names(self) -> tuple[str, ...]:
        return tuple(self._setups)

    def has_setup(self, setup_name: str) -> bool:
        return setup_name in self._setups

    def apply(self, player: Player, setup_name: str) -> None:
        setup = self._setups[setup_name]

        setup(player)

    def _setup_skilling(self, player: Player) -> None:
        items = (Bank()
            .add(ITEM_PARSER.get_instance('poor copper pickaxe', 1))
            .add(ITEM_PARSER.get_instance('poor iron pickaxe', 1))
            .add(ITEM_PARSER.get_instance('poor iron axe', 1))
            .add(ITEM_PARSER.get_instance('poor iron secateurs', 1))
            .add(ITEM_PARSER.get_instance('poor copper fishing rod', 1))
            .add(ITEM_PARSER.get_instance('poor iron fishing rod', 1))
            .add(ITEM_PARSER.get_instance('poor copper helm', 1))
        )

        player.give(items)


SETUP_MANAGER = SetupManager()
