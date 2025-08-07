from ...util.player.EquipmentSlot import EquipmentSlot


OFFHANDS = {
    'copper kiteshield': {
        'name': 'copper kiteshield',
        'equipment_slot': EquipmentSlot.OFFHAND,
        'tier': 1,
        'stats': {
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        },
    },
    'iron kiteshield': {
        'name': 'iron kiteshield',
        'equipment_slot': EquipmentSlot.OFFHAND,
        'tier': 10,
        'stats': {
            'physical_defense': 4,
            'magical_barrier': 0,
            'evasiveness': 1,
        },
    },
    'steel kiteshield': {
        'name': 'steel kiteshield',
        'equipment_slot': EquipmentSlot.OFFHAND,
        'tier': 15,
        'stats': {
            'physical_defense': 6,
            'magical_barrier': 0,
            'evasiveness': 1,
        },
    },
    'adamant kiteshield': {
        'name': 'adamant kiteshield',
        'equipment_slot': EquipmentSlot.OFFHAND,
        'tier': 30,
        'stats': {
            'physical_defense': 11,
            'magical_barrier': 0,
            'evasiveness': 2,
        },
    },
}
