from ...util.player.EquipmentSlot import EquipmentSlot


HELMS = {
    'copper helm': {
        'name': 'copper helm',
        'equipment_slot': EquipmentSlot.HELM,
        'tier': 1,
        'stats': {
            'physical_defense': 1,
            'magical_barrier': 0,
            'evasiveness': 0,
        },
    },
    'iron helm': {
        'name': 'iron helm',
        'equipment_slot': EquipmentSlot.HELM,
        'tier': 10,
        'stats': {
            'physical_defense': 3,
            'magical_barrier': 0,
            'evasiveness': 0,
        },
    },
    'steel helm': {
        'name': 'steel helm',
        'equipment_slot': EquipmentSlot.HELM,
        'tier': 15,
        'stats': {
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        },
    },
    'adamant helm': {
        'name': 'adamant helm',
        'equipment_slot': EquipmentSlot.HELM,
        'tier': 30,
        'stats': {
            'physical_defense': 7,
            'magical_barrier': 1,
            'evasiveness': 1,
        },
    },
}
