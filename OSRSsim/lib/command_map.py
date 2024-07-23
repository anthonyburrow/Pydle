from .activities import skilling

from .operations.bank import interface_bank
from .operations.skills import interface_skills
from .operations.tools import interface_tools

from .testing.skilling import testing_skilling


# Mapping
map_activity = {
    'mine': {
        'function': skilling.MiningActivity,
    },
    'chop': {
        'function': skilling.WoodcuttingActivity,
    },
    'collect': {
        'function': skilling.ForagingActivity,
    },
}

map_operations = {
    'bank': {
        'function': interface_bank,
        'aliases': ('b',),
    },
    'skills': {
        'function': interface_skills,
        'aliases': ('s', 'skill'),
    },
    'tools': {
        'function': interface_tools,
        'aliases': ('t', 'tool'),
    },
}

map_testing = {
    'skilling': {
        'function': testing_skilling,
    },
}


# Aliases
def populate_aliases(map_dict: dict) -> dict:
    alias_map = {}
    for command in map_dict:
        if 'aliases' not in map_dict[command]:
            continue
        aliases = map_dict[command]['aliases']
        for alias in aliases:
            alias_map[alias] = command
    return alias_map


alias_activity = populate_aliases(map_activity)
alias_operations = populate_aliases(map_operations)
alias_testing = populate_aliases(map_testing)
