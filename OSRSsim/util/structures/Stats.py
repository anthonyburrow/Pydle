from .Stat import Stat
from ..colors import color, COLOR_STATS


# { stat_key : (Formal name, Stat type) }
STATS = {
    # Gathering skills
    'mining': ('Mining', 'gathering'),
    'woodcutting': ('Woodcutting', 'gathering'),
    'foraging': ('Foraging', 'gathering'),
}


class Stats:

    def __init__(self):
        self._stats: dict = {}

    def get_stat(self, stat_key: str) -> Stat:
        return self._stats[stat_key]

    def get_stats(self) -> dict:
        return {stat_key: self.get_stat(stat_key) for stat_key in STATS}

    def get_stats_XP(self) -> dict:
        return {stat_key: self.get_stat(stat_key).XP for stat_key in STATS}

    def add_XP(self, stat_key: str, XP: float):
        return self.get_stat(stat_key).add_XP(XP)

    def set_XP(self, stat_key: str, XP: float):
        return self.get_stat(stat_key).set_XP(XP)

    def set_level(self, stat_key: str, level: int):
        return self.get_stat(stat_key).set_level(level)

    def get_level(self, stat_key: str) -> int:
        return self.get_stat(stat_key).level

    def load_stats(self, stats_dict: dict = None):
        for stat_key, stat_info in STATS.items():
            if stats_dict is None:
                self._stats[stat_key] = Stat(*stat_info)
                continue

            if stat_key not in stats_dict:
                self._stats[stat_key] = Stat(*stat_info)
                continue

            stat_XP = stats_dict[stat_key]
            self._stats[stat_key] = Stat(*stat_info, XP=stat_XP)

    @property
    def stats(self) -> dict:
        return self._stats

    def __str__(self):
        msg_out: list = []
        just_amount: int = max([len(s) for s in STATS])
        for stat_key in STATS:
            stat: Stat = self.get_stat(stat_key)
            name: str = color(stat.name, COLOR_STATS, justify=just_amount)
            stat_line: str = f'  {name} | Lvl {stat.level:<2} ({stat.XP:,.0f} EXP)'
            msg_out.append(stat_line)

        msg = '\n' + '\n'.join(msg_out) + '\n'

        return msg
