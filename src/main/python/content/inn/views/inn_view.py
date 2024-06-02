from content.inn.controllers.inn_controller import InnController
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView
from utils.print_utils import PrintUtils


class InnView:
    def __init__(self, inn):
        self.controller = InnController(inn)

    def display_options(self):
        PrintUtils.print_centered("Voce está em um Inn\n")
        PrintUtils.print_separator_line()
        print("1. Descansar")
        print("2. Abrir inventario")
        print("3. Abrir Journal")
        print("4. Sair")


    def handle_input(self):
        while True:
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                self.controller.rest()
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