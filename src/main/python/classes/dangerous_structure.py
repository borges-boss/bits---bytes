from base.structure import Structure

class DangerousStructure(Structure):
    def __init__(self, name, type, width, height, dificulty):
        super().__init__(name, type, width, height)
        self._dificulty = dificulty

    @property
    def dificulty(self):
        return self.dificulty

    @dificulty.setter
    def dificulty(self, value):
        self.dificulty = value