from content.dangerous_structures.models.dangerous_structure_model import DangerousStructureModel


class DangerousStructureController:
    def __init__(self, structure):
        self.model = DangerousStructureModel(structure)

    def explore(self):
        self.model.explore()

    def leave(self):
        self.model.leave()