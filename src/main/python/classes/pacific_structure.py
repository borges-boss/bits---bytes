from base.structure import Structure
from classes.npc import Npc
from typing import List

class PacificStructure(Structure):
    def __init__(self, name, type, width, height, npcs:List[Npc],city):
        super().__init__(name, type, width, height)
        self._npcs = npcs
        self._city = city


    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def npcs(self):
        return self.npcs

    @npcs.setter
    def dificulty(self, value):
        self.npcs = value


    def has_npcs(self):
        return len(self.npcs) > 0
