from base.scene import Scene


class City(Scene):
    
    def __init__(self, width, height, name, description, structures):
        super().__init__(width, height)
        self._name = name
        self._description = description
        self._structures = structures

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
    def structures(self):
        return self._structures

    @structures.setter
    def structures(self, value):
        self._structures = value
