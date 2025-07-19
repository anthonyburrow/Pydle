import traceback


INFO_SPACING = '  '


def print_debug(msg: str):
    if not msg:
        return
    print(f'DEBUG: {msg}')


def print_error(msg: str):
    if not msg:
        return
    print(f'Error: {msg}')
    print(traceback.format_exc())


def print_info(msg: str | tuple[str], multiline=False):
    if not msg:
        return

    if not multiline:
        return print(f'{INFO_SPACING}{msg}')

    # Gives 1 line of padding and adds INFO_SPACING to each line
    msg = msg.split('\n')
    msg = f'\n{INFO_SPACING}'.join(msg)
    print(f'\n{INFO_SPACING}{msg}\n')
