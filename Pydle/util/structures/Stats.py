from ..colors import color


STATS = {
    'ticks_per_action': {
        'name': 'Attack Speed',
        'default': 3,
    },
    'attack_melee': {
        'name': 'Melee Attack',
        'default': 0,
    },
    'attack_ranged': {
        'name': 'Ranged Attack',
        'default': 0,
    },
    'attack_magic': {
        'name': 'Magic Attack',
        'default': 0,
    },
    'strength_melee': {
        'name': 'Melee Strength',
        'default': 0,
    },
    'strength_ranged': {
        'name': 'Ranged Strength',
        'default': 0,
    },
    'strength_magic': {
        'name': 'Magic Strength',
        'default': 0,
    },
    'defense_melee': {
        'name': 'Melee Defense',
        'default': 0,
    },
    'defense_ranged': {
        'name': 'Ranged Defense',
        'default': 0,
    },
    'defense_magic': {
        'name': 'Magic Defense',
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
