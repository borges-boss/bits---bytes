from python.base.structure import Structure
from python.classes.npc import Npc
from typing import List

class PacificStructure(Structure):
    def __init__(self, name, type, width, height, npcs:List[Npc]):
        super().__init__(name, type, width, height)
        self._npcs = npcs

    @property
    def npcs(self):
        return self.npcs

    @npcs.setter
    def dificulty(self, value):
        self.npcs = value


    def has_npcs(self):
        return len(self.npcs) > 0
