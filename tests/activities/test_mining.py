from Pydle.util.structures.Player import Player
from Pydle.util.structures.Controller import Controller
from Pydle.util.input import parse_command

from Pydle.commands.activities.skilling import MiningActivity


def test_missing_pickaxe():
    # Setup
    player = Player(name='TestPlayer')

    player.set_level('mining', 99)
    controller = Controller(player)

    command = 'mine iron'
    command = parse_command(command)

    # Test no pickaxe
    activity = MiningActivity(player, controller.client_ID, *command['args'])
    result_setup = activity.setup()

    assert not result_setup.success

    # Test has pickaxe
    player.give('iron pickaxe')
    player.equip_tool('iron pickaxe')

    activity = MiningActivity(player, controller.client_ID, *command['args'])
    result_setup = activity.setup()

    assert result_setup.success


def test_misspelled_ore():
    # Setup
    player = Player(name='TestPlayer')

    player.set_level('mining', 99)
    controller = Controller(player)

    command = 'mine irn'
    command = parse_command(command)

    # Test misspelled command
    player.give('iron pickaxe')
    player.equip_tool('iron pickaxe')

    activity = MiningActivity(player, controller.client_ID, *command['args'])
    result_setup = activity.setup()

    assert not result_setup.success
