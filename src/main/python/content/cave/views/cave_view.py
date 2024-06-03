from content.cave.controllers.cave_controller import CaveController
from services.location_service import LocationService
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class CaveView:

    def __init__(self, previous_structure_view, cave):
        self.controller = CaveController()
        self.previous_structure_view = previous_structure_view
        self.is_running = True
        self.cave = cave

    def display_options(self):
        PrintUtils.print_centered("Voce está explorando uma caverna\n")
        PrintUtils.print_separator_line()
        print("1. Explore")
        print("2. Open Inventory")
        print("3. Open Journal")
        print("4. Leave")

    def handle_input(self):
        while self.is_running:
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                self.controller.explore()
            elif input_value == "2":
                self.controller.open_inventory()
            elif input_value == "3":
                self.controller.open_journal()
            elif input_value == "4":
                self.stop_view()
                LocationService.leave(self.previous_structure_view)
            else:
                print("Invalid option.")

    def init_view(self):
        self.is_running = True
        self.handle_input()


    def stop_view(self):
        self.is_running = False
