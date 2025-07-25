import numpy as np
from typing import Self

from .Bank import Bank
from ..item_registry import verify_item


class LootTable:

    def __init__(self):
        self._weighted_items = {}
        self._weighted_probabilities = None
        self._every_items = {}
        self._tertiary_items = {}

    def add(self, item: str, quantity: int = 1, weight: float = 1.) -> Self:
        verify_item(item)

        # This, or make the ability to add weight to the same item
        if item in self._weighted_items:
            raise KeyError(f'{item} already added to LootTable')

        self._weighted_items[item] = (weight, quantity)

        # Could be optimized to not do it every add...
        self._reset_weights()

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

    def roll(self, quantity: int = 1) -> Bank:
        loot = Bank()

        if self._every_items:
            loot.add(self._roll_every(quantity))

        if self._tertiary_items:
            loot.add(self._roll_tertiary(quantity))

        if self._weighted_items:
            loot.add(self._roll_weighted(quantity))

        return loot

    def _reset_weights(self) -> None:
        weights = tuple((self._weighted_items[item][0]
                         for item in self._weighted_items))
        weights = np.array(weights)
        self._weighted_probabilities = weights / weights.sum()

    def _roll_weighted(self, quantity) -> dict:
        drops = np.random.choice((*self._weighted_items,), quantity,
                                 p=self._weighted_probabilities)
        counted_drops, counts = np.unique(drops, return_counts=True)

        loot = {drop: self._weighted_items[drop][1] * count
                for drop, count in zip(counted_drops, counts)}

        return loot

    def _roll_every(self, quantity) -> dict:
        loot = {drop: quantity * self._every_items[drop]
                for drop in self._every_items}

        return loot

    def _roll_tertiary(self, quantity) -> dict:
        loot = {}

        for item, item_info in self._tertiary_items.items():
            probability, item_quantity = item_info

            rolls = np.random.rand(quantity)
            n_successful = (rolls < probability).sum()

            loot[item] = n_successful * item_quantity

        return loot
