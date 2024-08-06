import win32gui


def get_client_ID():
    return win32gui.GetForegroundWindow()


def client_focused(client_ID) -> bool:
    return client_ID == get_client_ID()
