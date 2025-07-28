from ....util.structures.Gatherable import Gatherable


class Fish(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


FISH = {
    'shrimp': Fish(
        name='raw shrimp',
        level=1,
        xp=12.5,
        gather_value=1.00,
    ),
    'herring': Fish(
        name='raw herring',
        level=10,
        xp=22.5,
        gather_value=0.83,
    ),
    'bass': Fish(
        name='raw bass',
        level=15,
        xp=35.,
        gather_value=0.69,
    ),
    'trout': Fish(
        name='raw trout',
        level=20,
        xp=50.,
        gather_value=0.56,
    ),
    'salmon': Fish(
        name='raw salmon',
        level=30,
        xp=65.,
        gather_value=0.46,
    ),
    'lobster': Fish(
        name='raw lobster',
        level=40,
        xp=85.,
        gather_value=0.37,
    ),
    'swordfish': Fish(
        name='raw swordfish',
        level=60,
        xp=125.,
        gather_value=0.29,
    ),
    'shark': Fish(
        name='raw shark',
        level=70,
        xp=175.,
        gather_value=0.22,
    ),
    'anglerfish': Fish(
        name='raw anglerfish',
        level=80,
        xp=240.,
        gather_value=0.16,
    ),
    'whale': Fish(
        name='raw whale',
        level=90,
        xp=350.,
        gather_value=0.11,
    ),

}
