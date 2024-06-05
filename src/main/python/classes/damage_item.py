from base.item import Item

class DamageItem(Item):

    def __init__(self, name, type: str, rarity: str, weight, enchantments, damage: float = 0.0):
        super().__init__(name, type, rarity, weight, enchantments)
        self._damage = damage


    def to_dict(self):
        return {
            'name': self._name,
            'type': self._type,
            'rarity': self._rarity,
            'weight': self._weight,
            'enchantments': [e.to_dict() for e in self._enchantments],
            'damage': self.damage
        }

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value
