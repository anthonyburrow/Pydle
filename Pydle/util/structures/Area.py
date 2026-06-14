from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from ...lib.skilling.fishing import FISH
from ...lib.skilling.foraging import COLLECTABLES
from ...lib.skilling.mining import ORES
from ...lib.skilling.woodcutting import LOGS
from ..colors import color, color_theme
from ..items.ItemInstance import ItemInstance
from ..monsters.MonsterInstance import MonsterInstance
from ..ticks import Ticks

if TYPE_CHECKING:
    from ..player.Player import Player


# Make dataclass
class Area:
    def __init__(
        self,
        name: str,
        coordinates: tuple[int, int],
        requirements: list[Callable[[Player], bool]] | None = None,
        # Combat
        monsters: set[str] | None = None,
        # Gatherables
        collectables: dict[str, int] | None = None,
        fish: set[str] | None = None,
        logs: set[str] | None = None,
        ores: set[str] | None = None,
    ):
        self.name: str = name
        self.coordinates: tuple[int, int] = coordinates
        self.requirements: list[Callable[[Player], bool]] = requirements or []
        # Combat
        self.monsters: set[str] = monsters or set()
        # Gatherables
        self.collectables: dict[str, int] = collectables or dict()
        self.fish: set[str] = fish or set()
        self.logs: set[str] = logs or set()
        self.ores: set[str] = ores or set()

    def travel_ticks(self, current_coordinates: tuple[int, int]) -> int:
        x0, y0 = current_coordinates
        x, y = self.coordinates

        time_sec = 60.0 * ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
        time_ticks = int(time_sec / Ticks()) + 1

        return time_ticks

    def contains_monster(self, monster_instance: MonsterInstance) -> bool:
        return monster_instance.name in self.monsters

    def contains_collectable(self, item_instance: ItemInstance) -> bool:
        return item_instance.name in self.collectables

    def contains_fish(self, item_instance: ItemInstance) -> bool:
        return item_instance.name in self.fish

    def contains_log(self, item_instance: ItemInstance) -> bool:
        return item_instance.name in self.logs

    def contains_ore(self, item_instance: ItemInstance) -> bool:
        return item_instance.name in self.ores

    def detailed_info(self) -> str:
        msg = []

        msg.append('-' * len(self.name))
        msg.append(str(self))
        msg.append('-' * len(self.name))
        msg.append('')

        if self.monsters:
            msg.append(f'{color("Monsters", color_theme["skill_combat"])}:')
            [msg.append(f'- {key.capitalize()}') for key in self.monsters]
            msg.append('')

        def append_gathering_block(
            label: str, items: set | dict, data_source: dict
        ):
            if not items:
                return
            msg.append(f'{color(label, color_theme["skill_gathering"])}:')

            just_amount: int = max([len(x) for x in self.collectables])
            for key in items:
                level = data_source[key].level
                msg.append(
                    f'- {key.capitalize():<{just_amount}} | Lvl {level}'
                )

        append_gathering_block('Foraging', self.collectables, COLLECTABLES)
        msg.append('')
        append_gathering_block('Fishing', self.fish, FISH)
        msg.append('')
        append_gathering_block('Woodcutting', self.logs, LOGS)
        msg.append('')
        append_gathering_block('Mining', self.ores, ORES)

        return '\n'.join(msg)

    def __str__(self) -> str:
        text: str = f'{self.name}'
        return color(text, color_theme['UI_1'])
