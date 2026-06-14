from collections.abc import Callable

from ...util.items.ItemParser import ITEM_PARSER
from ...util.player.Bank import Bank
from ...util.player.Player import Player
from ...util.player.SkillType import SkillType


class SetupManager:
    def __init__(self):
        self._setups: dict[str, Callable[[Player], None]] = {
            'restart': self._setup_restart,
            'skilling': self._setup_skilling,
            'tools': self._setup_tools,
        }

    def names(self) -> tuple[str, ...]:
        return tuple(self._setups)

    def has_setup(self, setup_name: str) -> bool:
        return setup_name in self._setups

    def apply(self, player: Player, setup_name: str) -> None:
        setup = self._setups[setup_name]

        setup(player)

    def _setup_restart(self, player: Player) -> None:
        player.remove_all_items()

    def _setup_skilling(self, player: Player) -> None:
        items: Bank = (
            Bank()
            .add(ITEM_PARSER.get_instance('copper bar', 1000))
            .add(ITEM_PARSER.get_instance('iron bar', 1000))
            .add(ITEM_PARSER.get_instance('steel bar', 1000))
        )

        player.give(items)

        player.set_level(SkillType.MINING, 50)
        player.set_level(SkillType.SMITHING, 50)
        player.set_level(SkillType.FISHING, 50)
        player.set_level(SkillType.COOKING, 50)
        player.set_level(SkillType.FORAGING, 50)
        player.set_level(SkillType.HERBLORE, 50)
        player.set_level(SkillType.WOODCUTTING, 50)
        player.set_level(SkillType.CRAFTING, 50)

    def _setup_tools(self, player: Player) -> None:
        items: Bank = (
            Bank()
            .add(ITEM_PARSER.get_instance('poor copper pickaxe', 1))
            .add(ITEM_PARSER.get_instance('poor iron pickaxe', 1))
            .add(ITEM_PARSER.get_instance('poor copper axe', 1))
            .add(ITEM_PARSER.get_instance('poor iron axe', 1))
            .add(ITEM_PARSER.get_instance('poor copper secateurs', 1))
            .add(ITEM_PARSER.get_instance('poor iron secateurs', 1))
            .add(ITEM_PARSER.get_instance('poor copper fishing rod', 1))
            .add(ITEM_PARSER.get_instance('poor iron fishing rod', 1))
        )

        player.give(items)


SETUP_MANAGER = SetupManager()
