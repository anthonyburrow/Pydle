from ....util.structures.Gatherable import Gatherable


class Collectable(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


COLLECTABLES = {
    'parsley': Collectable(
        name='parsley leaves',
        xp=5.,
        level=1,
    ),
    'clover': Collectable(
        name='clover bloom',
        xp=5.,
        level=1,
    ),
    'thyme': Collectable(
        name='thyme leaves',
        xp=12.5,
        level=10,
    ),
    'strawberry': Collectable(
        name='wild strawberry',
        xp=12.5,
        level=10,
    ),
    'sage': Collectable(
        name='sage leaves',
        xp=20.,
        level=15,
    ),
    'violet': Collectable(
        name='violet bloom',
        xp=20.,
        level=15,
    ),
    'rosemary': Collectable(
        name='rosemary leaves',
        xp=35.,
        level=20,
    ),
    'goldmoss': Collectable(
        name='goldmoss bloom',
        xp=35.,
        level=20,
    ),
    'lavender': Collectable(
        name='lavender bloom',
        xp=55.,
        level=30,
    ),
    'mulberries': Collectable(
        name='wild mulberries',
        xp=55.,
        level=30,
    ),
    'mugwort': Collectable(
        name='mugwort leaves',
        xp=75.,
        level=40,
    ),
    'raspberries': Collectable(
        name='black raspberries',
        xp=75.,
        level=40,
    ),
    'clove': Collectable(
        name='clove bud',
        xp=100.,
        level=50,
    ),
    'elderflower': Collectable(
        name='elderflower bloom',
        xp=100.,
        level=50,
    ),
    'reishi': Collectable(
        name='reishi cap',
        xp=125.,
        level=60,
    ),
    'nettle': Collectable(
        name='nettle leaves',
        xp=125.,
        level=60,
    ),
    'chanterelle': Collectable(
        name='golden chanterelle',
        xp=150.,
        level=70,
    ),
    'blackcurrant': Collectable(
        name='blackcurrant berries',
        xp=150.,
        level=70,
    ),
    'morel': Collectable(
        name='morel cap',
        xp=200.,
        level=80,
    ),
    'blueberries': Collectable(
        name='wild blueberries',
        xp=200.,
        level=80,
    ),
    'betony': Collectable(
        name='betony bloom',
        xp=250.,
        level=90,
    ),
    'belladonna': Collectable(
        name='belladonna leaf',
        xp=250.,
        level=90,
    ),
    'hawthorn': Collectable(
        name='hawthorn berries',
        xp=325.,
        level=100,
    ),
    'skullcap': Collectable(
        name='skullcap bloom',
        xp=325.,
        level=100,
    ),
    'lions_mane': Collectable(
        name="lion's mane cap",
        xp=400.,
        level=110,
    ),
    'rowan': Collectable(
        name='rowan berries',
        xp=400.,
        level=110,
    ),
    'truffle': Collectable(
        name='black truffle',
        xp=475.,
        level=120,
    ),
    'ghostcap': Collectable(
        name='ghostcap mushroom',
        xp=475.,
        level=120,
    ),
}
