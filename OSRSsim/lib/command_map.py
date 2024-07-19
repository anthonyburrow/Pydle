from .activities import skilling

from .operations.bank import interface_bank
from .operations.stats import interface_stats
from .operations.tools import interface_tools

from .testing.skilling import testing_skilling


map_activity = {
    'mine': skilling.MiningActivity,
    'chop': skilling.WoodcuttingActivity,
    'collect': skilling.ForagingActivity,
}

map_operations = {
    'bank': interface_bank,
    'stats': interface_stats,
    'tools': interface_tools,
}

map_testing = {
    'skilling': testing_skilling,
}
