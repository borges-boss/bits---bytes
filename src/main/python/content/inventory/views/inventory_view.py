from content.inventory.controllers.inventory_controller import InventoryController
from utils.print_utils import PrintUtils

class InventoryView:
    def __init__(self):
        self.controller = InventoryController()

    def display_items(self):
        items = self.controller.get_player_items()
        PrintUtils.print_centered("Inventario\n")
        PrintUtils.print_separator_line()
        print("\n")
        for i, item in enumerate(items, start=1):
            print(f"{i}. Item: {item.name}, Peso: {item.weight} Kg")
            

    def handle_input(self):
        while True:
            self.display_items()
            print("\nDigite o numero do item que quer equipar ou usar, ou digite 'q' para sair:")
            user_input = input()
            if user_input.lower() == 'q':
                break
            try:
                item_number = int(user_input)
                items = self.controller.get_player_items()
                if 1 <= item_number <= len(items):
                    item = items[item_number - 1]
                    self.controller.use_item(item)
                    self.controller.equip_item(item)
                else:
                    print("\nNumero de item invalido.")
            except ValueError:
                print("\nInput invalido. Por favor digite apenas numeros")


    def init_view(self):
        self.display_items()
        self.handle_input()


