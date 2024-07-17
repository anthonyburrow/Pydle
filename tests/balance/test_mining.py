import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from OSRSsim.util.ticks import Ticks

from OSRSsim.lib.data.skilling.mining import ores, pickaxes


def get_XP_rate(probability, XP, ticks_per_ore):
    n_ticks = 3600. / Ticks()
    n_attempts = int(n_ticks / ticks_per_ore)
    n_success = int(n_attempts * probability)
    total_xp = n_success * XP
    return total_xp


def test_probability_curve():
    fig, ax = plt.subplots(2, 1, dpi=125, figsize=(6.4, 6.), sharex=True)

    levels = np.arange(1, 127)

    for ore, pickaxe in zip(ores.values(), pickaxes.values()):
        probs = np.array([ore.prob_success(lvl, pickaxe['power'], pickaxe['level']) for lvl in levels])
        xp_rates = np.array([get_XP_rate(p, ore.XP, pickaxe['ticks_per_use']) for p in probs])

        ax[0].plot(levels, probs, '-', ms=1.5, label=ore.name)
        ax[1].plot(levels, xp_rates, '-', ms=1.5)

    # pickaxe = pickaxes['Iron pickaxe']
    # pickaxe = pickaxes['Elder pickaxe']
    # ore = ores['orikalkum']
    # probs = np.array([ore.prob_success(lvl, pickaxe['power'], pickaxe['level']) for lvl in levels])
    # xp_rates = np.array([get_XP_rate(p, ore.XP, pickaxe['ticks_per_use']) for p in probs])

    # ax[0].plot(levels, probs, '-', ms=1.5, label=ore.name)
    # ax[1].plot(levels, xp_rates, '-', ms=1.5)

    ax[0].xaxis.set_major_locator(MultipleLocator(10))
    ax[0].xaxis.set_minor_locator(MultipleLocator(2))

    ax[1].yaxis.set_major_locator(MultipleLocator(20000))
    ax[1].yaxis.set_minor_locator(MultipleLocator(2500))

    ax[1].set_xlabel('Level')
    ax[0].set_ylabel('probability of success')
    ax[1].set_ylabel('XP rate')

    ax[0].set_xlim(1, 126)
    ax[0].set_ylim(0., 1.)
    ax[1].set_ylim(bottom=0.)

    ax[0].legend()

    plt.tight_layout()

    fn = './tests/balance/mining_xp.png'
    fig.savefig(fn)
