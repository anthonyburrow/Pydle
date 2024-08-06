from ..colors import color


STATS = {
    'attack_melee': 'Melee Attack',
    'attack_ranged': 'Ranged Attack',
    'attack_magic': 'Magic Attack',
    'strength_melee': 'Melee Strength',
    'strength_ranged': 'Ranged Strength',
    'strength_magic': 'Magic Strength',
    'defense_melee': 'Melee Defense',
    'defense_ranged': 'Ranged Defense',
    'defense_magic': 'Magic Defense',
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

    def __str__(self):
        msg: list = []
        just_amount: int = max([len(s) for s in STATS])
        for stat_key, stat_name in STATS.items():
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
