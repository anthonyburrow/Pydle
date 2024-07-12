from ..lib.command_map import map_activity


def parse_command(msg: str) -> dict:
    msg = msg.lower()
    msg = msg.split(' ')

    command = msg[0]

    if command in map_activity:
        return {
            'type': 'activity',
            'activity': map_activity[command],
            'args': tuple(msg[1:]),
        }
    else:
        return {
            'type': None,
        }
