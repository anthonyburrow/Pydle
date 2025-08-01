from ....util.structures.Gatherable import Gatherable


class Fish(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


FISH = {
    'shrimp': Fish(
        name='raw shrimp',
        xp=5.,
        level=1,
    ),
    'anchovy': Fish(
        name='raw anchovy',
        xp=12.5,
        level=10,
    ),
    'trout': Fish(
        name='raw trout',
        xp=20.,
        level=15,
    ),
    'cod': Fish(
        name='raw cod',
        xp=35.,
        level=20,
    ),
    'catfish': Fish(
        name='raw catfish',
        xp=55.,
        level=30,
    ),
    'bass': Fish(
        name='raw bass',
        xp=75.,
        level=40,
    ),
    'salmon': Fish(
        name='raw salmon',
        xp=100.,
        level=50,
    ),
    'lobster': Fish(
        name='raw lobster',
        xp=125.,
        level=60,
    ),
    'barracuda': Fish(
        name='raw barracuda',
        xp=150.,
        level=70,
    ),
    'tuna': Fish(
        name='raw bluefin tuna',
        xp=200.,
        level=80,
    ),
    'marlin': Fish(
        name='raw marlin',
        xp=250.,
        level=90,
    ),
    'anglerfish': Fish(
        name='raw anglerfish',
        xp=325.,
        level=100,
    ),
    'shark': Fish(
        name='raw great white shark',
        xp=400.,
        level=110,
    ),
    'coelacanth': Fish(
        name='raw coelacanth',
        xp=475.,
        level=120,
    ),
}

