from ..visuals import centered_title


STATS = {
    'physical_strength': {
        'name': 'Physical Strength',
    },
    'physical_defense': {
        'name': 'Physical Defense',
    },
    'magical_power': {
        'name': 'Magical Power',
    },
    'magical_barrier': {
        'name': 'Magical Barrier',
    },
    'accuracy': {
        'name': 'Accuracy',
    },
    'evasiveness': {
        'name': 'Evasiveness',
    },
}


class Stats(dict):

    def __init__(self, stats_dict: dict = None, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        stats_dict = stats_dict or {}

        for stat_key in STATS:
            self[stat_key] = stats_dict.get(stat_key, 0)

    def reset(self):
        for stat_key in STATS:
            self[stat_key] = 0

    def __str__(self):
        msg: list = []

        max_stat_length: int = max([len(x) for x in self])
        max_value_length: int = max([len(str(x)) for x in self.values()])
        total_length = max_stat_length + max_value_length + 3

        msg.append(centered_title('STATS', total_length))

        for stat_key, stat_info in STATS.items():
            stat_name = stat_info['name']
            value = self[stat_key]
            msg.append(f'{stat_name:>{max_stat_length}} | {value:>{max_value_length}}')

        msg = '\n'.join(msg)

        return msg

    def __add__(self, other_stats):
        for stat in STATS:
            self[stat] += other_stats[stat]
        return self

    def __eq__(self, other):
        if isinstance(other, Stats):
            return dict(self) == dict(other)
        if isinstance(other, dict):
            return dict(self) == other
        return NotImplemented

    def __setitem__(self, key, value):
        if key not in STATS:
            raise KeyError(f'Invalid skill key: "{key}"')
        super().__setitem__(key, int(value))
