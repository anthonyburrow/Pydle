from ...util.structures import Player
from ...util.output import print_output
from ...util.colors import color, COLOR_STATS
from .. import stats


def stats_print(player: Player, stat=None):
    if stat is not None:
        print_output(player.get_stat(stat))
        return

    msg_out = []
    just_amount = max([len(s) for s in stats])
    for _stat in stats:
        stat = player.get_stat(_stat)
        name = color(stat.name, COLOR_STATS, justify=just_amount)
        stat_line = f'  {name} | Lvl {stat.level:<2} ({stat.XP:,.0f} EXP)'
        msg_out.append(stat_line)

    print_output('\n' + '\n'.join(msg_out) + '\n')
