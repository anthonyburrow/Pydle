

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

    'mithril helm',
    'mithril chestplate',
    'mithril platelegs',
    'mithril gauntlets',
    'mithril boots',
    'mithril longsword',
    'mithril kiteshield',

    'adamant helm',
    'adamant chestplate',
    'adamant platelegs',
    'adamant gauntlets',
    'adamant boots',
    'adamant longsword',
    'adamant kiteshield',

    'rune helm',
    'rune chestplate',
    'rune platelegs',
    'rune gauntlets',
    'rune boots',
    'rune longsword',
    'rune kiteshield',

    'orikalkum helm',
    'orikalkum chestplate',
    'orikalkum platelegs',
    'orikalkum gauntlets',
    'orikalkum boots',
    'orikalkum longsword',
    'orikalkum kiteshield',

    'necronium helm',
    'necronium chestplate',
    'necronium platelegs',
    'necronium gauntlets',
    'necronium boots',
    'necronium longsword',
    'necronium kiteshield',

    'bane helm',
    'bane chestplate',
    'bane platelegs',
    'bane gauntlets',
    'bane boots',
    'bane longsword',
    'bane kiteshield',

    'elder helm',
    'elder chestplate',
    'elder platelegs',
    'elder gauntlets',
    'elder boots',
    'elder longsword',
    'elder kiteshield',

    'leather gloves',

    #
    # Tools
    #
    'copper fishing rod',
    'iron fishing rod',
    'steel fishing rod',
    'mithril fishing rod',
    'adamant fishing rod',
    'rune fishing rod',
    'orikalkum fishing rod',
    'necronium fishing rod',
    'bane fishing rod',
    'elder fishing rod',

    'copper secateurs',
    'iron secateurs',
    'steel secateurs',
    'mithril secateurs',
    'adamant secateurs',
    'rune secateurs',
    'orikalkum secateurs',
    'necronium secateurs',
    'bane secateurs',
    'elder secateurs',

    'copper pickaxe',
    'iron pickaxe',
    'steel pickaxe',
    'mithril pickaxe',
    'adamant pickaxe',
    'rune pickaxe',
    'orikalkum pickaxe',
    'necronium pickaxe',
    'bane pickaxe',
    'elder pickaxe',

    'copper axe',
    'iron axe',
    'steel axe',
    'mithril axe',
    'adamant axe',
    'rune axe',
    'orikalkum axe',
    'necronium axe',
    'bane axe',
    'elder axe',

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
    'iron ore',
    'coal',
    'mithril ore',
    'adamantite ore',
    'runite ore',
    'orikalkum ore',
    'necronium ore',
    'bane ore',
    'elder ore',

    'copper bar',
    'iron bar',
    'steel bar',
    'mithril bar',
    'adamantite bar',
    'runite bar',
    'orikalkum bar',
    'necronium bar',
    'bane bar',
    'elder bar',

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
