import pickle
from pathlib import Path

from .Bank import Bank
from .Skills import Skills
from .Skill import Skill
from .Tools import Tools
from .Tool import Tool
from .Equipment import Equipment
from .Stats import Stats
from .UpdatedEffects import UpdatedEffects
from ..colors import color, color_theme
from ..Result import Result
from ...lib.areas import HOME_AREA


_default_save_file = 'character.save'


class Player:

    def __init__(self, save_file: str = None, *args, **kwargs):
        if save_file is None:
            save_file = _default_save_file
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
    def add_xp(self, *args, **kwargs) -> dict:
        return self._skills.add_xp(*args, **kwargs)

    def set_xp(self, *args, **kwargs):
        return self._skills.set_xp(*args, **kwargs)

    def set_level(self, *args, **kwargs):
        return self._skills.set_level(*args, **kwargs)

    def get_skill(self, *args, **kwargs) -> Skill:
        return self._skills.get_skill(*args, **kwargs)

    def get_level(self, *args, **kwargs) -> int:
        return self._skills.get_level(*args, **kwargs)

    @property
    def skills(self) -> Skills:
        return self._skills

    # Combat
    @property
    def hitpoints(self) -> int:
        return self._hitpoints

    def get_max_hitpoints(self) -> int:
        return 90 + 10 * self.get_skill('hitpoints').level

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

    def get_tool(self, *args, **kwargs) -> Tool:
        return self._tools.get_tool(*args, **kwargs)

    @property
    def tools(self) -> Tools:
        return self._tools

    # Equipment
    def equip(self, *args, **kwargs) -> Result:
        return self._equipment.equip(*args, **kwargs)

    def unequip(self, *args, **kwargs) -> Result:
        return self._equipment.unequip(*args, **kwargs)

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
    def new_load(self, name: str = None, *args, **kwargs):
        if name is None:
            self._name: str = input('Character name?\n> ')
        else:
            self._name: str = name

        self._area: str = HOME_AREA

        self._bank: Bank = Bank()

        self._skills: Skills = Skills()
        self._skills.load_skills()

        self._tools: Tools = Tools(self)
        self._tools.load_tools()

        self._equipment: Equipment = Equipment(self)
        self._equipment.load_equipment()

        self._updated_effects: UpdatedEffects = UpdatedEffects()

    def load(self, *args, **kwargs):
        if not Path(self.save_file).is_file():
            return self.new_load(*args, **kwargs)

        with open(self.save_file, 'rb') as file:
            save_input: dict = pickle.load(file)

        self._name: str = save_input['name']

        if 'area' in save_input:
            self._area: str = save_input['area']
        else:
            self._area: str = HOME_AREA

        self._bank: Bank = Bank(save_input['items'])

        self._skills: Skills = Skills()
        if 'skills' in save_input:
            self._skills.load_skills(save_input['skills'])
        else:
            self._skills.load_skills()

        self._tools: Tools = Tools(self)
        if 'tools' in save_input:
            self._tools.load_tools(save_input['tools'])
        else:
            self._tools.load_tools()

        self._equipment: Equipment = Equipment(self)
        if 'equipment' in save_input:
            self._equipment.load_equipment(save_input['equipment'])
        else:
            self._equipment.load_equipment()

        self._updated_effects: UpdatedEffects = UpdatedEffects()
        if 'updated_effects' in save_input:
            self._updated_effects.load_effects(save_input['updated_effects'])

    def save(self):
        save_output: dict = {
            'name': self.name,
            'area': self.area,
            'items': self._bank.get_items(),
            'skills': self._skills.get_skills_xp(),
            'tools': self._tools.get_tools_names(),
            'equipment': self._equipment.get_equipment_names(),
            'updated_effects': self._updated_effects.get_effects(),
        }

        with open(self.save_file, 'wb') as file:
            pickle.dump(save_output, file)

    # Misc
    def __str__(self):
        text: str = f'{self.name}'
        return color(text, color_theme['player'])
