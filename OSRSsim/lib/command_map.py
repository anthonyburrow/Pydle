from .activities.skilling import MiningActivity

from .info.bank import bank_print

from .testing.skilling import testing_skilling


map_activity = {
    'mine': MiningActivity,
}

map_info = {
    'bank': bank_print
}

map_testing = {
    'skilling': testing_skilling
}
