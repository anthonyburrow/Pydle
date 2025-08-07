import numpy as np
from typing import Self

from ..items.Item import ItemInstance
from ..player.Bank import Bank


class LootTable:

    def __init__(self):
        self._weighted_items: list[ItemInstance | None] = []
        self._weighted_weights: list[float] = []
        self._weighted_probabilities: np.ndarray | None = None
        self._needs_reset: bool = True

        self._every_items = list[ItemInstance] = []
        self._tertiary_items: list[tuple[ItemInstance, float]] = []

    def add(self, item_instance: ItemInstance, weight: float = 1.) -> Self:
        self._weighted_items.append(item_instance)
        self._weighted_weights.append(weight)

        self._needs_reset = True

        return self

    def add_empty(self, weight: float = 1.) -> Self:
        self._weighted_items.append(None)
        self._weighted_weights.append(weight)

        self._needs_reset = True

        return self

    def tertiary(self, item_instance: ItemInstance, probability: float) -> Self:
        self._tertiary_items.append((item_instance, probability))

        return self

    def every(self, item_instance: ItemInstance) -> Self:
        self._every_items.append(item_instance)

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

    def _roll_weighted(self, n_rolls: int) -> ItemInstance | Bank:
        if self._needs_reset:
            self._reset_weighted_probs()

        index = np.random.choice(
            len(self._weighted_items),
            size=n_rolls,
            p=self._weighted_probabilities,
        )

        if n_rolls == 1:
            index = index[0]
            item_instance: ItemInstance | None = self._weighted_items[index]
            return item_instance or Bank()

        loot: Bank = Bank()
        for i in index:
            item_instance: ItemInstance | None = self._weighted_items[i]
            if item_instance is None:
                continue

            loot.add(item_instance)

        return loot

    def _roll_every(self, n_rolls: int) -> Bank:
        loot: Bank = Bank()

        for item_instance in self._every_items:
            if n_rolls == 1:
                loot.add(item_instance)
                continue

            new_quantity: int = n_rolls * item_instance.quantity
            new_instance: ItemInstance = item_instance.copy(quantity=new_quantity)

            loot.add(new_instance)

        return loot

    def _roll_tertiary(self, n_rolls: int) -> Bank:
        loot: Bank = Bank()

        for item_instance, probability in self._tertiary_items:
            rolls: np.ndarray = np.random.rand(n_rolls)
            n_successful: int = (rolls < probability).sum()

            if not n_successful:
                continue

            if n_rolls == 1:
                loot.add(item_instance)
                continue

            new_quantity: int = n_successful * item_instance.quantity
            new_instance: ItemInstance = item_instance.copy(quantity=new_quantity)

            loot.add(new_instance)

        return loot
