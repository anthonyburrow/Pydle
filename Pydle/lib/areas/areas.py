from ...util.structures.Area import Area


HOME_AREA = 'hearthmere'

areas = {
    'hearthmere': Area(
        name='Hearthmere',
        coordinates=(0, 0),
        monsters={
            'goblin',
        },
        fish={
            'shrimp',
        },
        herbs={
            'guam',
        },
        logs={
            'logs',
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
