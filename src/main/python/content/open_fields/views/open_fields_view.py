from content.open_fields.controllers.open_fields_controller import OpenFieldsController
from utils.print_utils import PrintUtils


class OpenFieldsView:
    def __init__(self):
        self.controller = OpenFieldsController()

    def display_options(self):
        print("Voce esta em um campo aberto")
        print("1. Explore")
        print("2. Open Inventory")
        print("3. Open Journal")
        print("4. Leave")

    def handle_input(self, input):
        if input == "1":
            self.controller.explore()
        elif input == "2":
            self.controller.open_inventory()
        elif input == "3":
            self.controller.open_journal()
        elif input == "4":
            self.controller.leave()
        else:
            print("Invalid option.")
            return False
        
        return True

    def init_view(self):
        self.display_options()
        input = None
        input_valid  = False
        PrintUtils.print_separator_line()
        print("\n")
        while input_valid == False:
            input = input("Escolha uma opção: ")
            input_valid = self.handle_input(input)