from models.pacific_structure_model import PacificStructureModel

class PacificStructureController:
    def __init__(self, structure):
        self.model = PacificStructureModel(structure)

    def visit_inn(self):
        self.model.visit_inn()

    def visit_shop(self):
        self.model.visit_shop()

    def visit_tavern(self):
        self.model.visit_tavern()

    def leave_city(self):
        self.model.leave_city()