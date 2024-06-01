from content.dungeon.controllers.dungeon_controller import DungeonController
from utils.print_utils import PrintUtils


class DungeonView:
    def __init__(self, dungeon):
        self.controller = DungeonController(dungeon)
        self.dungeon = dungeon

    def display_options(self):
        print("Voce está na dangeon "+self.dungeon.name)
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