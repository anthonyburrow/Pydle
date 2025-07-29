from dataclasses import dataclass


@dataclass
class Result:
    success: bool = True
    msg: str = ''
