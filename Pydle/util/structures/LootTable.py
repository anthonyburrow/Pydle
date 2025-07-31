import numpy as np
from typing import Self

from .Bank import Bank
from ..item_registry import verify_item


class LootTable:

    def __init__(self):
        self._weighted_items: list[str | None] = []
        self._weighted_quantities: list[int] = []
        self._weighted_weights: list[float] = []
        self._weighted_probabilities: np.ndarray | None = None
        self._needs_reset = True

        self._every_items = {}
        self._tertiary_items = {}

    def add(self, item: str, quantity: int = 1, weight: float = 1.) -> Self:
        verify_item(item)

        if item in self._weighted_items:
            raise KeyError(f'{item} already added to LootTable.')

        self._weighted_items.append(item)
        self._weighted_quantities.append(quantity)
        self._weighted_weights.append(weight)

        self._needs_reset = True

        return self

    def add_empty(self, weight: float = 1.) -> Self:
        if None in self._weighted_items:
            raise KeyError(f'Empty weight already added to LootTable.')

        self._weighted_items.append(None)
        self._weighted_quantities.append(0)
        self._weighted_weights.append(weight)

        self._needs_reset = True

        return self

    def tertiary(self, item: str, probability: float, quantity: int = 1) -> Self:
        verify_item(item)

        if item in self._tertiary_items:
            raise KeyError(f'{item} already added to LootTable')

        self._tertiary_items[item] = (probability, quantity)

        return self

    def every(self, item: str, quantity: int = 1) -> Self:
        verify_item(item)

        if item in self._every_items:
            raise KeyError(f'{item} already added to LootTable')

        self._every_items[item] = quantity

        return self

    def roll(self, n_rolls: int = 1) -> Bank:
        loot = Bank()

        if self._every_items:
            loot.add(self._roll_every(n_rolls))

        if self._tertiary_items:
            loot.add(self._roll_tertiary(n_rolls))

        if self._weighted_items:
            loot.add(self._roll_weighted(n_rolls))

        return loot

    def _reset_weighted_probs(self) -> None:
        weights = np.array(self._weighted_weights, dtype=np.float64)
        self._weighted_probabilities = weights / weights.sum()

        self._needs_reset = False

    def _roll_weighted(self, n_rolls: int) -> dict:
        if self._needs_reset:
            self._reset_weighted_probs()

        index = np.random.choice(
            len(self._weighted_items),
            size=n_rolls,
            p=self._weighted_probabilities,
        )

        if n_rolls == 1:
            index = index[0]
            item = self._weighted_items[index]
            quantity = self._weighted_quantities[index]
            return {} if item is None else {item: quantity}

        result = Bank()
        for i in index:
            item = self._weighted_items[i]
            if item is None:
                continue
            quantity = self._weighted_quantities[i]
            result.add(item, quantity)

        return result

    def _roll_every(self, n_rolls: int) -> dict:
        loot = {
            drop: n_rolls * self._every_items[drop]
            for drop in self._every_items
        }

        return loot

    def _roll_tertiary(self, n_rolls: int) -> dict:
        loot = {}

        for item, item_info in self._tertiary_items.items():
            probability, item_quantity = item_info

            rolls = np.random.rand(n_rolls)
            n_successful = (rolls < probability).sum()

            loot[item] = int(n_successful * item_quantity)

        return loot
