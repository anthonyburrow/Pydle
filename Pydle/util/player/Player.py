from dataclasses import dataclass, asdict
import json
from pathlib import Path
from typing import Self

from .Bank import Bank
from .Equipment import Equipment
from .Skill import Skill
from .Skills import Skills
from .SkillType import SkillType
from .Stats import Stats
from .Tools import Tools
from .UpdatedEffects import UpdatedEffects
from ..colors import color, color_theme
from ..Result import Result
from ..items.ItemInstance import ItemInstance
from ..structures.UserInterface import COMMAND_PREFIX
from ...lib.areas import HOME_AREA
from ...lib.item_sets import NEW_PLAYER_ITEMS


@dataclass
class PlayerSaveData:
    name: str
    area: str
    items: dict
    skills: dict
    tools: dict
    equipment: dict
    updated_effects: dict

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(
            name=data.get('name', 'UNNAMED'),
            area=data.get('area', HOME_AREA),
            items=data.get('items', {}),
            skills=data.get('skills', {}),
            tools=data.get('tools', {}),
            equipment=data.get('equipment', {}),
            updated_effects=data.get('updated_effects', {}),
        )


class Player:

    def __init__(self, save_file: str = None, *args, **kwargs):
        self.save_file: str = save_file

        self.load(*args, **kwargs)

        self.heal_full()

    # Player
    @property
    def name(self) -> str:
        return self._name

    # Area
    @property
    def area(self) -> str:
        return self._area

    def set_area(self, area: str) -> None:
        self._area = area

    # Skills and Experience
    def add_xp(self, skill_type: SkillType, xp: float) -> dict:
        return self._skills.add_xp(skill_type, xp)

    def set_xp(self, skill_type: SkillType, xp: float):
        return self._skills.set_xp(skill_type, xp)

    def get_level(self, skill_type: SkillType) -> int:
        return self._skills.get_level(skill_type)

    def set_level(self, skill_type: SkillType, level: int):
        return self._skills.set_level(skill_type, level)

    def get_skill(self, skill_type: SkillType) -> Skill:
        return self._skills[skill_type]

    @property
    def skills(self) -> Skills:
        return self._skills

    # Combat
    @property
    def hitpoints(self) -> int:
        return self._hitpoints

    def get_max_hitpoints(self) -> int:
        return 90 + 10 * self.get_skill(SkillType.HITPOINTS).level

    def heal(self, amount: int) -> None:
        max_hp = self.get_max_hitpoints()
        self._hitpoints = min(max_hp, self._hitpoints + amount)

    def heal_full(self) -> None:
        self._hitpoints = self.get_max_hitpoints()

    def damage(self, amount: int) -> None:
        self._hitpoints = max(0, self._hitpoints - amount)

    # Items
    def give(self, *args, **kwargs):
        self._bank.add(*args, **kwargs)

    def remove(self, *args, **kwargs):
        self._bank.remove(*args, **kwargs)

    def has(self, *args, **kwargs) -> bool:
        return self._bank.contains(*args, **kwargs)

    @property
    def bank(self) -> Bank:
        return self._bank

    # Tools
    def equip_tool(self, *args, **kwargs) -> Result:
        return self._tools.equip(*args, **kwargs)

    def unequip_tool(self, *args, **kwargs) -> Result:
        return self._tools.unequip(*args, **kwargs)

    def get_tool(self, *args, **kwargs) -> ItemInstance | None:
        return self._tools.get(*args, **kwargs)

    @property
    def tools(self) -> Tools:
        return self._tools

    # Equipment
    def equip(self, *args, **kwargs) -> Result:
        return self._equipment.equip(*args, **kwargs)

    def unequip(self, *args, **kwargs) -> Result:
        return self._equipment.unequip(*args, **kwargs)

    def get_equipment(self, *args, **kwargs) -> ItemInstance | None:
        return self._equipment.get(*args, **kwargs)

    @property
    def equipment(self) -> Equipment:
        return self._equipment

    # Equipment stats
    @property
    def stats(self) -> Stats:
        return self._equipment.stats

    def get_stat(self, stat_key: str) -> int:
        return self.stats[stat_key]

    # Updated effects
    def add_effect(self, *args, **kwargs):
        return self._updated_effects.add_effect(*args, **kwargs)

    def remove_effect(self, *args, **kwargs):
        return self._updated_effects.remove_effect(*args, **kwargs)

    def has_effect(self, *args, **kwargs) -> bool:
        return self._updated_effects.has_effect(*args, **kwargs)

    def update_effects(self, *args, **kwargs):
        return self._updated_effects.update_effects(*args, **kwargs)

    @property
    def updated_effects(self) -> UpdatedEffects:
        return self._updated_effects

    # Management
    def load_new_player(self, name: str = None, *args, **kwargs):
        self._name: str = name or input(f'Character name?\n{COMMAND_PREFIX}')
        self._area: str = HOME_AREA
        self._bank: Bank = Bank().add(NEW_PLAYER_ITEMS)
        self._skills: Skills = Skills()
        self._tools: Tools = Tools(self)
        self._equipment: Equipment = Equipment(self)
        self._updated_effects: UpdatedEffects = UpdatedEffects()

        self.save()

    def load(self, *args, **kwargs):
        if not self.save_file:
            return self.load_new_player(*args, **kwargs)

        if not Path(self.save_file).is_file():
            return self.load_new_player(*args, **kwargs)

        with open(self.save_file, 'r') as file:
            data = json.load(file)
        save_data = PlayerSaveData.from_dict(data)

        self._name: str = save_data.name
        self._area: str = save_data.area
        self._bank: Bank = Bank(save_data.items)
        self._skills: Skills = Skills(save_data.skills)
        self._tools: Tools = Tools(self, save_data.tools)
        self._equipment: Equipment = Equipment(self, save_data.equipment)
        self._updated_effects: UpdatedEffects = UpdatedEffects(save_data.updated_effects)

    def save(self):
        if not self.save_file:
            return

        save_data = PlayerSaveData(
            name=self.name,
            area=self.area,
            items=self._bank.to_dict(),
            skills=self._skills.to_dict(),
            tools=self._tools.to_dict(),
            equipment=self._equipment.to_dict(),
            updated_effects=self._updated_effects.to_dict(),
        )

        with open(self.save_file, 'w') as file:
            json.dump(save_data.to_dict(), file, indent=4)

    # Misc
    def __str__(self):
        return color(self.name, color_theme['player'])
