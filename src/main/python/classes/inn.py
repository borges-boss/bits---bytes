from classes.npc import Npc
from classes.pacific_structure import PacificStructure

class Inn(PacificStructure):

    def __init__(self, name, type, width, height, inkeeper: Npc, rooms, price_per_stay, city):
        super().__init__(name, type, width, height, [], city)
        self._inkeeper = inkeeper
        self._rooms = rooms
        self._price_per_stay = price_per_stay

    @property
    def inkeeper(self):
        return self._inkeeper

    @inkeeper.setter
    def inkeeper(self, value):
        self._inkeeper = value

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    @property
    def price_per_stay(self):
        return self._price_per_stay

    @price_per_stay.setter
    def price_per_stay(self, value):
        self._price_per_stay = value



    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'width': self.width,
            'height': self.height,
            'inkeeper': self._inkeeper.to_dict(),
            'rooms': self.rooms,
            'price_per_stay': self.price_per_stay,
            'city': self.city
        }
