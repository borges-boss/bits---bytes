from classes.dangerous_structure import DangerousStructure


class Dungeon(DangerousStructure):

    def __init__(self, name, type, dificulty, chests_opened, layers, bosses, chest_count, monsters):
        super().__init__(name, type, dificulty)
        self._chests_opened = chests_opened
        self._layers = layers
        self._bosses = bosses
        self._chest_count = chest_count
        self._monsters = monsters


    @property
    def monsters(self):
        return self._monsters

    @monsters.setter
    def monsters(self, value):
        self._monsters = value

    @property
    def chests_opened(self):
        return self._chests_opened

    @chests_opened.setter
    def chests_opened(self, value):
        self._chests_opened = value

    @property
    def layers(self):
        return self._layers

    @layers.setter
    def layers(self, value):
        self._layers = value

    @property
    def bosses(self):
        return self._bosses

    @bosses.setter
    def bosses(self, value):
        self._bosses = value

    @property
    def chest_count(self):
        return self._chest_count

    @chest_count.setter
    def chest_count(self, value):
        self._chest_count = value


