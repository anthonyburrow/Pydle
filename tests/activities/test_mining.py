from OSRSsim.util.structures import Player, Controller
from OSRSsim.util.input import parse_command

from OSRSsim.lib.activities.skilling import MiningActivity


def test_missing_pickaxe():
    # Setup
    player = Player(name='TestPlayer')
    player.set_level('mining', 99)
    controller = Controller(player)

    command = 'mine iron'
    command = parse_command(command)

    # Test no pickaxe
    activity = MiningActivity(controller, *command['args'])
    status = activity.setup()

    assert not status['success']

    # Test has pickaxe
    player.give('Iron pickaxe')

    activity = MiningActivity(controller, *command['args'])
    status = activity.setup()

    assert status['success']


def test_misspelled_ore():
    # Setup
    player = Player(name='TestPlayer')
    player.set_level('mining', 99)
    controller = Controller(player)

    command = 'mine irn'
    command = parse_command(command)

    # Test misspelled command
    player.give('Iron pickaxe')

    activity = MiningActivity(controller, *command['args'])
    status = activity.setup()

    assert not status['success']
