from controllers.pacific_structure_controller import PacificStructureController

class PacificStructureView:
    def __init__(self, structure):
        self.controller = PacificStructureController(structure)

    def display_options(self):
        print("1. Visit Inn")
        print("2. Visit Shop")
        print("3. Visit Tavern")
        print("4. Leave City")

    def handle_input(self, input):
        if input == "1":
            self.controller.visit_inn()
        elif input == "2":
            self.controller.visit_shop()
        elif input == "3":
            self.controller.visit_tavern()
        elif input == "4":
            self.controller.leave_city()
        else:
            print("Invalid option.")