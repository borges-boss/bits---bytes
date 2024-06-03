from content.inn.controllers.inn_controller import InnController
from services.location_service import LocationService
from utils.print_utils import PrintUtils
from utils.console_utils import ConsoleUtils

class InnView:
    def __init__(self, previous_structure_view, inn):
        self.controller = InnController()
        self.previous_structure_view = previous_structure_view
        self.inn = inn
        self.is_running = True

    def display_options(self):
        PrintUtils.print_centered("Voce está em um Inn\n")
        PrintUtils.print_separator_line()
        print("1. Descansar")
        print("2. Abrir inventario")
        print("3. Abrir Journal")
        print("4. Sair")


    def handle_input(self):
        while True:
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                self.controller.rest()
            elif input_value == "2":
                self.controller.open_inventory()
            elif input_value == "3":
                self.controller.open_journal()
            elif input_value == "4":
                self.stop_View()
                LocationService.leave(self.previous_structure_view)
                break
            else:
                print("Invalid option.")

    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_View(self):
     self.is_running = False