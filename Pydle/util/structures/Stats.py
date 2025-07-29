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

    def __init__(self, stats: dict = None, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        for stat_key in STATS:
            if stats is None:
                self[stat_key] = 0
            elif stat_key not in stats:
                self[stat_key] = 0
            else:
                self[stat_key] = stats[stat_key]

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

    def __setitem__(self, key: str, value: int):
        if key not in STATS:
            return
        super().__setitem__(key, int(value))

    def __add__(self, other_stats):
        for stat in STATS:
            self[stat] += other_stats[stat]
        return self
