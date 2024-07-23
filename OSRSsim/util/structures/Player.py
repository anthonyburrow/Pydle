import pickle
from pathlib import Path

from .Bank import Bank
from .Skills import Skills
from .Skill import Skill
from .Tools import Tools
from .Tool import Tool
from ..colors import color, COLOR_CHARACTER


_default_save_file = 'character.save'


class Player:

    def __init__(self, save_file: str = None, *args, **kwargs):
        if save_file is None:
            save_file = _default_save_file
        self.save_file: str = save_file

        self.load(*args, **kwargs)

    # Player
    @property
    def name(self) -> str:
        return self._name

    # Skills and Experience
    def add_XP(self, *args, **kwargs) -> dict:
        return self._skills.add_XP(*args, **kwargs)

    def set_XP(self, *args, **kwargs):
        return self._skills.set_XP(*args, **kwargs)

    def set_level(self, *args, **kwargs):
        return self._skills.set_level(*args, **kwargs)

    def get_skill(self, *args, **kwargs) -> Skill:
        return self._skills.get_skill(*args, **kwargs)

    def get_level(self, *args, **kwargs) -> int:
        return self._skills.get_level(*args, **kwargs)

    @property
    def skills(self) -> Skills:
        return self._skills

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
    def add_tool(self, *args, **kwargs):
        return self._tools.add(*args, **kwargs)

    def remove_tool(self, *args, **kwargs):
        return self._tools.remove(*args, **kwargs)

    def get_tool(self, *args, **kwargs) -> Tool:
        return self._tools.get_tool(*args, **kwargs)

    @property
    def tools(self) -> Tools:
        return self._tools

    # Management
    def new_load(self, name: str = None, *args, **kwargs):
        if name is None:
            self._name: str = input('Character name?\n> ')
        else:
            self._name: str = name

        self._bank: Bank = Bank()

        self._skills: Skills = Skills()
        self._skills.load_skills()

        self._tools: Tools = Tools(self)
        self._tools.load_tools()

    def load(self, *args, **kwargs):
        if not Path(self.save_file).is_file():
            return self.new_load(*args, **kwargs)

        with open(self.save_file, 'rb') as file:
            save_input: dict = pickle.load(file)

        self._name: str = save_input['name']

        self._bank: Bank = Bank(save_input['items'])

        self._skills: Skills = Skills()
        self._skills.load_skills(save_input['skills'])

        self._tools: Tools = Tools(self)
        self._tools.load_tools(save_input['tools'])

    def save(self):
        save_output: dict = {
            'name': self.name,
            'items': self._bank.items,
            'skills': self._skills.get_skills_XP(),
            'tools': self._tools.get_tools_names(),
        }

        with open(self.save_file, 'wb') as file:
            pickle.dump(save_output, file)

    # Misc
    def __str__(self):
        text: str = f'{self._name}'
        return color(text, COLOR_CHARACTER)
