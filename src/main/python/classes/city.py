from base.scene import Scene


class City(Scene):
    
    def __init__(self, width, height, name, description, structure_count):
        super().__init__(width, height)
        self._name = name
        self._description = description
        self._structure_count = structure_count

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def structure_count(self):
        return self._structure_count

    @structure_count.setter
    def structure_count(self, value):
        self._structure_count = value
