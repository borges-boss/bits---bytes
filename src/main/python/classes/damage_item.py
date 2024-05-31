from typing import List
from base.enchantment import Enchantment
from base.item import Item

class DamageItem(Item):

    def __init__(self, name, type, rarity, weight, enchantments: List[Enchantment], damage: float = 0.0):
        super().__init__(name, type, rarity, weight, enchantments)
        self._damage = damage


    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value
