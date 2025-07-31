

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
    'blackirn pickaxe',
    'wyrmheart pickaxe',
    'valnorite pickaxe',
    'kharadant pickaxe',

    'copper axe',
    'iron axe',
    'steel axe',
    'adamant axe',
    'blackirn axe',
    'wyrmheart axe',
    'valnorite axe',
    'kharadant axe',

    #
    # Herbs
    #
    'parsley leaves',
    'clover bloom',
    'thyme leaves',
    'wild strawberry',
    'sage leaves',
    'violet bloom',
    'rosemary leaves',
    'goldmoss bloom',
    'lavender bloom',
    'wild mulberries',
    'mugwort leaves',
    'black raspberries',
    'clove bud',
    'elderflower bloom',
    'reishi cap',
    'nettle leaves',
    'blackcurrant berries',
    'morel cap',
    'wild blueberries',
    'betony bloom',
    'belladonna leaf',
    'hawthorn berries',
    'skullcap bloom',
    "lion's mane cap",
    'rowan berries',
    'black truffle',
    'ghostcap mushroom',

    #
    # Logs
    #
    'pine log',
    'birch log',
    'maple log',
    'willow log',
    'oak log',
    'elm log',
    'yew log',
    'bloodwood log',
    'ironwood log',
    'ashen log',
    'heartwood log',
    'glassthorn log',
    'emberpine log',
    'ebonspire log',

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
