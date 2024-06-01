from content.inn.controllers.inn_controller import InnController
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView
from utils.print_utils import PrintUtils


class InnView:
    def __init__(self, inn):
        self.controller = InnController(inn)

    def display_options(self):
        print("You are currently in the Inn.")
        print("1. Rest")
        print("2. Open Inventory")
        print("3. Open Journal")
        print("4. Leave")

    def handle_input(self, input):
        if input == "1":
            self.controller.rest()
        elif input == "2":
            self.controller.open_inventory()
        elif input == "3":
            self.controller.open_journal()
        elif input == "4":
            self.controller.leave()
        else:
            print("Invalid option.")


    def init_view(self):
        self.display_options()
        input = None
        input_valid  = False
        PrintUtils.print_separator_line()
        print("\n")
        while input_valid == False:
            input = input("Escolha uma opção: ")
            input_valid = self.handle_input(input)