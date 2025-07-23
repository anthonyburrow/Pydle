from ..colors import color


STATS = {
    'attack_speed': {
        'name': 'Attack Speed',
        'default': 3,
    },
    'physical_strength': {
        'name': 'Physical Strength',
        'default': 0,
    },
    'physical_defense': {
        'name': 'Physical Defense',
        'default': 0,
    },
    'magical_power': {
        'name': 'Magical Power',
        'default': 0,
    },
    'magical_barrier': {
        'name': 'Magical Barrier',
        'default': 0,
    },
    'accuracy': {
        'name': 'Accuracy',
        'default': 0,
    },
    'evasiveness': {
        'name': 'Evasiveness',
        'default': 0,
    },
}


class Stats(dict):

    def __init__(self, stats: dict = None, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        for stat_key in STATS:
            if stats is None:
                self[stat_key] = STATS[stat_key]['default']
            elif stat_key not in stats:
                self[stat_key] = STATS[stat_key]['default']
            else:
                self[stat_key] = stats[stat_key]

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

    def __setitem__(self, key: str, value: int):
        if key not in STATS:
            return
        super().__setitem__(key, int(value))

    def __add__(self, other_stats):
        for stat in STATS:
            self[stat] += other_stats[stat]
        return self
