# Pydle

A RuneScape-esque CLI (terminal-based) idle game written in Python.

Currently, many RuneScape ideas and content are implemented into this, but I
expect many changes, deviations, and additions as it evolves.


## Installation and Running

Clone the source and install with `pip`:

```
git clone https://github.com/anthonyburrow/Pydle.git
cd Pydle
pip install .
```

This creates a `pydle` script that should be added to your path. You can run
this script from anywhere to run the game:

```
pydle
```

This game was built on Python 3.13.5 for Windows, and requires the following
Python packages (which are installed with `pip install .`):
- `numpy`
- `pynput`
- `pywin32` (Windows) / `python-xlib` (Linux)
- `colorama`
- `platformdirs`

Player data is written to a "player.json" file which is saved in the
`platformdirs` user data directory:
- Windows: `C:\Users\<username>\AppData\Local\Pydle\Pydle`
- Linux: `~/.local/share/Pydle/Pydle`


## In the Game

The game begins with the user giving a name to their character. This begins a
save file for this character, which is loaded anytime the game starts again.

For a list of available commands, use `help` or `?`.

The the CLI and game can be closed with the `exit` command.
