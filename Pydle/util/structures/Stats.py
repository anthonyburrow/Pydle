from ..colors import color


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
        just_amount: int = max([len(s) for s in STATS])
        for stat_key, stat_info in STATS.items():
            stat_name = stat_info['name']
            name = color(
                stat_name,
                '',
                justify=just_amount
            )
            value = self[stat_key]
            msg.append(f'{name} : {value}')

        msg = '\n'.join(msg)

        return msg

    def __add__(self, other_stats):
        for stat in STATS:
            self[stat] += other_stats[stat]
        return self

    def __setitem__(self, key, value):
        if key not in STATS:
            raise KeyError(f'Invalid skill key: "{key}"')
        super().__setitem__(key, int(value))
