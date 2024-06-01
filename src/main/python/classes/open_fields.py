from classes.dangerous_structure import DangerousStructure
from base.item import Item
from typing import List
from classes.monster import Monster

class OpenFields(DangerousStructure):

    def __init__(self, name, type, width, height, dificulty, loot:List[Item],monsters:List[Monster]):
        super().__init__(name, type, width, height, dificulty)
        self._loot = loot
        self._monsters = monsters

    @property
    def loot(self):
        return self._loot

    @loot.setter
    def loot(self, value):
        self._loot = value

    @property
    def monsters(self):
        return self._monsters

    @monsters.setter
    def monsters(self, value):
        self._monsters = value
