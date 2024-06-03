from typing import List
from classes.pacific_structure import PacificStructure
from classes.npc import Npc


class CityStructure(PacificStructure):

    def __init__(self, name, type, width, height, npcs: List[Npc]):
        super().__init__(name, type, width, height, npcs)