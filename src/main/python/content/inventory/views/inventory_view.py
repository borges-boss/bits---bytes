from content.inventory.controllers.inventory_controller import InventoryController
from content.player.controllers.player_controller import PlayerController
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils

class InventoryView:
    def __init__(self):
        self.controller = InventoryController()
        self.is_running = True

    def display_items(self):
        items = self.controller.get_player_items()
        PrintUtils.print_centered("Inventario\n")
        PrintUtils.print_separator_line()
        print("\n")
        print("Nome: "+PlayerController.get_player().name+ 
              "\t|\tRaca: "+PlayerController.get_player().race+ 
              "\t|\tClasse: "+PlayerController.get_player().game_class+ 
              "\t|\tCoins: "+ str(PlayerController.get_player().wallet.coins))
        print("\n")
        for i, item in enumerate(items, start=1):
            print(f"{i}. Item: {item.name}, Peso: {item.weight}")
            

    def handle_input(self):
        while self.is_running:
            ConsoleUtils.clear_terminal()
            self.display_items()
            print("\nDigite o numero do item que quer equipar ou usar, ou digite 'q' para sair:")
            user_input = input()
            if user_input.lower() == 'q':
                self.stop_View()
                break
            try:
                item_number = int(user_input)
                items = self.controller.get_player_items()
                if 1 <= item_number <= len(items):
                    item = items[item_number - 1]
                    self.controller.use_item(item)
                    self.controller.equip_item(item)
                    PlayerController.init_player_attributes() #Re-calcular player stats para considerar o item que voce acabou de equipar
                else:
                    print("\nNumero de item invalido.")
            except ValueError:
                print("\nInput invalido. Por favor digite apenas numeros")


    def init_view(self):
        self.is_running = True
        self.handle_input()


    def stop_View(self):
        self.is_running = False



