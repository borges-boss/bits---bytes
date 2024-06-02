from content.open_fields.controllers.open_fields_controller import OpenFieldsController
from python.services.location_service import LocationService
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class OpenFieldsView:
    def __init__(self):
        self.is_running = True
        self.controller = OpenFieldsController()

    def display_options(self):
        PrintUtils.print_centered("Voce esta em um campo aberto\n")
        PrintUtils.print_separator_line()
        print("1. Explorar")
        print("2. Abrir Inventario")
        print("3. Abrir Journal")
        print("4. Viajar")


    def handle_input(self):
        while True:
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
                LocationService.travel()
                break
            else:
                print("Invalid option.")

    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_view(self):
        self.is_running = False