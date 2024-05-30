from python.classes.dangerous_structure import DangerousStructure
from python.base.item import Item
from typing import List
from python.classes.monster import Monster

class OpenFields(DangerousStructure):

    def __init__(self, name, type, dificulty, loot:List[Item],monsters:List[Monster]):
        super().__init__(name, type, dificulty)
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
