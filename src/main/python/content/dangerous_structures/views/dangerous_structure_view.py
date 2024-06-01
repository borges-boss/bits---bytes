from content.dangerous_structures.controllers.dangerous_structure_controller import DangerousStructureController


class DangerousStructureView:
    def __init__(self, structure):
        self.controller = DangerousStructureController(structure)

    def display_options(self):
        print("1. Explorar")
        print("2. Sair")

    def handle_input(self, input):
        if input == "1":
            self.controller.explore()
        elif input == "2":
            self.controller.leave()
        else:
            print("Invalid option.")