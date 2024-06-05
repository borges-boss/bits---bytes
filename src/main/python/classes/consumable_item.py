from base.item import Item

class ConsumableItem(Item):

    def __init__(self, name, type, rarity, weight, consumable_type, effect_value, effect_type):
        super().__init__(name, type, rarity, weight, [])
        self._consumable_type = consumable_type
        self._effect_value = effect_value
        self._effect_type = effect_type


    @property
    def effect_type(self):
        return self._effect_type

    @effect_type.setter
    def effect_type(self, value):
        self._effect_type = value

    @property
    def consumable_type(self):
        return self._consumable_type

    @consumable_type.setter
    def consumable_type(self, value):
        self._consumable_type = value

    @property
    def effect_value(self):
        return self._effect_value

    @effect_value.setter
    def effect_value(self, value):
        self._effect_value = value



    def to_dict(self):
        return {
            'name': self._name,
            'type': self._type,
            'rarity': self._rarity,
            'weight': self._weight,
            'enchantments': [],
            'consumable_type': self._consumable_type,
            'effect_value': self._effect_value,
            'effect_type': self._effect_type
        }