from Pydle.commands.Command import Command
from Pydle.commands.operations import testing as testing_operation_module
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.SkillType import SkillType


class CaptureUI:
    def __init__(self):
        self.messages: list[str] = []

    def print(self, message: str):
        self.messages.append(message)


def test_setup_requires_argument(test_player):
    ui = CaptureUI()
    command = Command.parse('testing setup')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert ui.messages[-1] == 'A setup name is needed. Use `testing setup [name]`.'


def test_setup_unknown_name_prints_available(test_player):
    ui = CaptureUI()
    command = Command.parse('testing setup unknown')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert 'Unknown setup `unknown`.' in ui.messages[-1]
    assert 'skilling' in ui.messages[-1]


def test_setup_skilling_applies_and_prints_success(test_player):
    ui = CaptureUI()
    command = Command.parse('testing setup skilling')
    pickaxe = ITEM_PARSER.get_instance('poor copper pickaxe')

    assert not test_player.has(pickaxe)

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert test_player.has(pickaxe)
    assert ui.messages
    assert ui.messages[-1] == 'Applied testing setup `skilling`.'


def test_set_level_success(test_player):
    ui = CaptureUI()
    command = Command.parse('testing set_level mining 25')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert test_player.get_level(SkillType.MINING) == 25
    assert ui.messages
    assert ui.messages[-1] == 'Set Mining to level 25.'


def test_set_level_invalid_skill(test_player):
    ui = CaptureUI()
    command = Command.parse('testing set_level nope 10')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert ui.messages[-1] == 'Invalid skill `nope`.'


def test_set_level_invalid_level_value(test_player):
    ui = CaptureUI()
    command = Command.parse('testing set_level mining abc')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert ui.messages[-1] == 'Invalid level `abc`.'


def test_set_level_missing_args(test_player):
    ui = CaptureUI()
    command = Command.parse('testing set_level')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert ui.messages[-1] == 'Usage: `testing set_level [skill] [level]`.'
