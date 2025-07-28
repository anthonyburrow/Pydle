import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from Pydle.util.ticks import Ticks

from Pydle.lib.skilling.mining import ORES, PICKAXES


def get_xp_rate(probability, xp, ticks_per_ore):
    n_ticks = 3600. / Ticks()
    n_attempts = int(n_ticks / ticks_per_ore)
    n_success = int(n_attempts * probability)
    total_xp = n_success * xp
    return total_xp


def test_probability_curve():
    fig, ax = plt.subplots(2, 1, dpi=125, figsize=(6.4, 6.), sharex=True)

    levels = np.arange(1, 127)

    for ore, pickaxe in zip(ORES.values(), PICKAXES.values()):
        probs = np.array([ore.prob_success(lvl, pickaxe) for lvl in levels])
        xp_rates = np.array([get_xp_rate(p, ore.xp, pickaxe.ticks_per_use) for p in probs])

        ax[0].plot(levels, probs, '-', ms=1.5, label=ore.name)
        ax[1].plot(levels, xp_rates, '-', ms=1.5)

    # pickaxe = PICKAXES['Iron pickaxe']
    # pickaxe = PICKAXES['Elder pickaxe']
    # ore = ORES['orikalkum']
    # probs = np.array([ore.prob_success(lvl, pickaxe['power'], pickaxe['level']) for lvl in levels])
    # xp_rates = np.array([get_xp_rate(p, ore.xp, pickaxe['ticks_per_use']) for p in probs])

    # ax[0].plot(levels, probs, '-', ms=1.5, label=ore.name)
    # ax[1].plot(levels, xp_rates, '-', ms=1.5)

    ax[0].xaxis.set_major_locator(MultipleLocator(10))
    ax[0].xaxis.set_minor_locator(MultipleLocator(2))

    ax[1].yaxis.set_major_locator(MultipleLocator(20000))
    ax[1].yaxis.set_minor_locator(MultipleLocator(2500))

    ax[1].set_xlabel('Level')
    ax[0].set_ylabel('probability of success')
    ax[1].set_ylabel('xp rate')

    ax[0].set_xlim(1, 126)
    ax[0].set_ylim(0., 1.)
    ax[1].set_ylim(bottom=0.)

    ax[0].legend()

    plt.tight_layout()

    fn = './tests/balance/mining_xp.png'
    fig.savefig(fn)
