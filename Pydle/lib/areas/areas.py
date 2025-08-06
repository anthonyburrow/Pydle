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
            'parsley leaves': 3,
            'thyme leaves': 1,
        },
        fish={
            'raw shrimp',
        },
        logs={
            'pine log',
        },
        ores={
            'copper ore',
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
