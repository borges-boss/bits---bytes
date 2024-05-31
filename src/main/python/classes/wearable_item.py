from typing import List
from base.enchantment import Enchantment
from base.item import Item

class WearableItem(Item):

    def __init__(self, name, type, rarity, weight, enchantments: List[Enchantment], defence: float = 0.0, wearable_type = ""):
        super().__init__(name, type, rarity, weight, enchantments)
        self._defence = defence
        self._wearable_type = wearable_type


    @property
    def wearable_type(self):
        return self._wearable_type

    @wearable_type.setter
    def wearable_type(self, value):
        self._wearable_type = value

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        self._defence = value



