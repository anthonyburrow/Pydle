from .activities import skilling

from .operations.bank import interface_bank
from .operations.skills import interface_skills
from .operations.tools import interface_tools

from .testing.skilling import testing_skilling


# Mapping
map_activity = {
    'mine': skilling.MiningActivity,
    'chop': skilling.WoodcuttingActivity,
    'collect': skilling.ForagingActivity,
}

map_operations = {
    'bank': interface_bank,
    'skills': interface_skills,
    'tools': interface_tools,
}

map_testing = {
    'skilling': testing_skilling,
}

# Aliases
alias_operations = {
    'b': 'bank',
    's': 'skills',
    'skill': 'skills',
    't': 'tools',
    'tool': 'tools',
}
