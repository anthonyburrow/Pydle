from dataclasses import dataclass

from ..items.Quality import Quality


@dataclass(frozen=True)
class BankKey:
    item_id: str
    quality: Quality | None = None

    def __str__(self) -> str:
        if not self.quality:
            return self.item_id
        return f'{self.quality} {self.item_id}'

    def __hash__(self):
        return hash((self.item_id, self.quality))
