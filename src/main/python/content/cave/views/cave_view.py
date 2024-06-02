from content.cave.controllers.cave_controller import CaveController
from utils.print_utils import PrintUtils


class CaveView:
    def __init__(self):
        self.controller = CaveController()

    def display_options(self):
        PrintUtils.print_centered("Voce está explorando uma caverna\n")
        PrintUtils.print_separator_line()
        print("1. Explore")
        print("2. Open Inventory")
        print("3. Open Journal")
        print("4. Leave")

    def handle_input(self):
        while True:
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                self.controller.explore()
            elif input_value == "2":
                self.controller.open_inventory()
            elif input_value == "3":
                self.controller.open_journal()
            elif input_value == "4":
                self.controller.leave()
                break
            else:
                print("Invalid option.")

    def init_view(self):
        self.display_options()
        PrintUtils.print_separator_line()
        print("\n")
        self.handle_input()