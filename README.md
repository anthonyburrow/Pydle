# OSRSsim

A RuneScape-esque CLI (terminal-based) idle game written in Python.

Currently, many RuneScape ideas and content are implemented into this, but I
expect many changes, deviations, and additions as it evolves.


## Installation and Running

Currently, it's best to download the source, navigate to the root directory,
and run the main entry-point file with `python ./OSRSsim.py`.

This game was built on Python 3.10, and requires the following Python packages:
- `NumPy`
- `keyboard`


## In the Game

The game begins with the user giving a name to their character. This begins a
save file for this character saved in `<root>/profile/`, which is loaded
anytime the game starts again.

For a list of available commands, use `help` or `?`.

The the CLI and game can be closed with the `exit` command.

