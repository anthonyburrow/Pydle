import asyncio

from OSRSsim.lib.activities import MiningActivity
from OSRSsim.util import Player


def test_missing_pickaxe():
    player = Player()

    ore = 'Iron ore'
    generic_params = {
        'player': player
    }
    activity = MiningActivity(ore, **generic_params)

    output = activity.setup()

    assert not output['able']


def test_normal():
    player = Player()
    player.bank.add('Iron pickaxe')

    ore = 'Iron ore'
    generic_params = {
        'player': player
    }
    activity = MiningActivity(ore, **generic_params)

    output = activity.setup()
    assert output['able']

    # Remove later
    if not output['able']:
        return

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(activity.begin())

    msg = activity.finish()
    print(msg)


if __name__ == '__main__':
    test_normal()
