from classes.dangerous_structure import DangerousStructure

class Cave(DangerousStructure):

    def __init__(self, name, type, dificulty, monsters, ores):
        super().__init__(name, type,200, 200, dificulty)
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
