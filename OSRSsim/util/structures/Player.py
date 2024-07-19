import pickle

from .Bank import Bank
from .Stat import Stat
from .Tools import Tools
from ..colors import color, COLOR_CHARACTER, COLOR_STATS
from ...lib import stats


class Player:

    def __init__(self, save_file: str = None, name: str = None):
        if name is None:
            name: str = input('Character name?\n> ')
        self.name = name

        if save_file is None:
            save_file = 'character.save'
        self.save_file: str = save_file

        self._bank: Bank = Bank()
        self._tools: Tools = Tools(self)

        self._stats = {}
        self._setup_stats()

    # Stats and Experience
    def add_XP(self, stat: str, XP: float):
        return self._stats[stat].add_XP(XP)

    def set_XP(self, stat: str, XP: float):
        self._stats[stat].set_XP(XP)

    def set_level(self, stat: str, level: int):
        self._stats[stat].set_level(level)

    def get_stat(self, stat: str) -> Stat:
        return self._stats[stat]

    def get_level(self, stat: str) -> int:
        return self.get_stat(stat).level

    def print_stats(self) -> str:
        msg_out: list = []
        just_amount: int = max([len(s) for s in stats])
        for _stat in stats:
            stat = self.get_stat(_stat)
            name: str = color(stat.name, COLOR_STATS, justify=just_amount)
            stat_line: str = f'  {name} | Lvl {stat.level:<2} ({stat.XP:,.0f} EXP)'
            msg_out.append(stat_line)

        msg = '\n' + '\n'.join(msg_out) + '\n'

        return msg

    def _setup_stats(self):
        for stat, stat_info in stats.items():
            if stat not in self._stats:
                self._stats[stat] = Stat(*stat_info)

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

    def get_tool(self, *args, **kwargs) -> str:
        return self._tools.get_tool(*args, **kwargs)

    @property
    def tools(self) -> Tools:
        return self._tools

    # Management
    def update(self):
        '''Done to update the previous player save to new version of code.'''
        self._setup_stats()

    def save(self):
        with open(self.save_file, 'wb') as file:
            pickle.dump(self, file)

    # Misc
    def __str__(self):
        text: str = f'{self.name}'
        return color(text, COLOR_CHARACTER)
