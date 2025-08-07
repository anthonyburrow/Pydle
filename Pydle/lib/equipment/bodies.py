from ...util.player.EquipmentSlot import EquipmentSlot


BODIES = {
    'copper chestplate': {
        'name': 'copper chestplate',
        'equipment_slot': EquipmentSlot.BODY,
        'tier': 1,
        'stats': {
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        },
    },
    'iron chestplate': {
        'name': 'iron chestplate',
        'equipment_slot': EquipmentSlot.BODY,
        'tier': 10,
        'stats': {
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        },
    },
    'steel chestplate': {
        'name': 'steel chestplate',
        'equipment_slot': EquipmentSlot.BODY,
        'tier': 15,
        'stats': {
            'physical_defense': 6,
            'magical_barrier': 1,
            'evasiveness': 1,
        },
    },
    'adamant chestplate': {
        'name': 'adamant chestplate',
        'equipment_slot': EquipmentSlot.BODY,
        'tier': 30,
        'stats': {
            'physical_defense': 11,
            'magical_barrier': 2,
            'evasiveness': 2,
        },
    },
}
