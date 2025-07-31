from ...util.structures.Area import Area


HOME_AREA = 'hearthmere'

AREAS = {
    'hearthmere': Area(
        name='Hearthmere',
        coordinates=(0, 0),
        monsters={
            'goblin',
        },
        collectables={
            'parsley': 3,
            'thyme': 1,
        },
        fish={
            'shrimp',
        },
        logs={
            'pine',
        },
        ores={
            'copper',
        },
    ),
    'eastveil': Area(
        name='Eastveil',
        coordinates=(0, 1),
        monsters={
            'goblin',
        },
    ),
}
