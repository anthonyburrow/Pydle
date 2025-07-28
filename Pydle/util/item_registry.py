

ITEMS = {
    #
    # Equipment
    #
    'copper helm',
    'copper chestplate',
    'copper platelegs',
    'copper gauntlets',
    'copper boots',
    'copper longsword',
    'copper kiteshield',

    'iron helm',
    'iron chestplate',
    'iron platelegs',
    'iron gauntlets',
    'iron boots',
    'iron longsword',
    'iron kiteshield',

    'steel helm',
    'steel chestplate',
    'steel platelegs',
    'steel gauntlets',
    'steel boots',
    'steel longsword',
    'steel kiteshield',

    'adamant helm',
    'adamant chestplate',
    'adamant platelegs',
    'adamant gauntlets',
    'adamant boots',
    'adamant longsword',
    'adamant kiteshield',

    'leather gloves',

    #
    # Tools
    #
    'copper fishing rod',
    'iron fishing rod',
    'steel fishing rod',
    'adamant fishing rod',

    'copper secateurs',
    'iron secateurs',
    'steel secateurs',
    'adamant secateurs',

    'copper pickaxe',
    'iron pickaxe',
    'steel pickaxe',
    'adamant pickaxe',

    'copper axe',
    'iron axe',
    'steel axe',
    'adamant axe',

    #
    # Herbs
    #
    'grimy guam',
    'guam',
    'grimy marrentill',
    'marrentill',
    'grimy harralander',
    'harralander',
    'grimy ranarr',
    'ranarr',
    'grimy toadflax',
    'toadflax',
    'grimy irit',
    'irit',
    'grimy kwuarm',
    'kwuarm',
    'grimy snapdragon',
    'snapdragon',
    'grimy torstol',
    'torstol',
    'grimy fellstalk',
    'fellstalk',

    #
    # Logs
    #
    'logs',
    'oak logs',
    'willow logs',
    'teak logs',
    'maple logs',
    'acadia logs',
    'mahogany logs',
    'yew logs',
    'magic logs',
    'elder logs',

    #
    # Fish
    #
    'shrimp',
    'raw shrimp',
    'herring',
    'raw herring',
    'bass',
    'raw bass',
    'trout',
    'raw trout',
    'salmon',
    'raw salmon',
    'lobster',
    'raw lobster',
    'swordfish',
    'raw swordfish',
    'shark',
    'raw shark',
    'anglerfish',
    'raw anglerfish',
    'whale',
    'raw whale',

    #
    # Ores
    #
    'copper ore',
    'silver ore',
    'iron ore',
    'coal',
    'gold ore',
    'adamantite ore',
    'black ore',
    'wyrmheart ore',
    'valnorite ore',
    'kharad ore',

    'copper bar',
    'silver bar',
    'iron bar',
    'steel bar',
    'gold bar',
    'adamantite bar',
    'blackirn bar',
    'wyrmheart bar',
    'valnorite bar',
    'kharadant bar',

    #
    # Crafting
    #
    'raw hide',
    'leather',

    #
    # Potion supplies
    #
    'vial',
    'eye of newt',

    #
    # Potions
    #
    'attack potion',

    #
    # Bones
    #
    'bones',

    #
    # Miscellaneous
    #
    'coins',
}


def verify_item(item: str) -> None:
    if item not in ITEMS:
        raise ValueError(f'"{item}" is not a valid item --- check registry.')
