from python.classes.dangerous_structure import DangerousStructure
from python.classes.monster import Monster
from python.base.item import Item
from typing import List


class Cave(DangerousStructure):

    def __init__(self, name, type, dificulty, monsters:List[Monster], ores:List[Item]):
        super().__init__(name, type, dificulty)
        self._monsters = monsters
        self._ores = ores

    @property
    def monsters(self):
        return self._monsters

    @monsters.setter
    def monsters(self, value):
        self._monsters = value

    @property
    def ores(self):
        return self._ores

    @ores.setter
    def ores(self, value):
        self._ores = value
