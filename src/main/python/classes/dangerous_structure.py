from python.base.structure import Structure

class DangerousStructure(Structure):
    def __init__(self, name, type, width, height, dificulty):
        super().__init__(name, type, width, height)
        self.dificulty = dificulty

    def __init__(self, name, type, dificulty):
        super().__init__(name, type)
        self.dificulty = dificulty

    @property
    def dificulty(self):
        return self.dificulty

    @dificulty.setter
    def dificulty(self, value):
        self.dificulty = value