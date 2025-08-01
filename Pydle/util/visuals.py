

def centered_title(title: str, total_length: int) -> str:
    pad = total_length - len(title) - 4
    left = pad // 2
    right = pad - left
    fill = '='
    return f'{fill * left}[ {title} ]{fill * right}\n'
