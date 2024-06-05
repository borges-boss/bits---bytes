from content.shop.controllers.shop_controller import ShopController
from content.player.controllers.player_controller import PlayerController
from services.location_service import LocationService
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils

class ShopView:
    def __init__(self,previous_structure_view, shop):
        self.controller = ShopController()
        self.previous_structure_view = previous_structure_view
        self.is_running = True
        self.shop = shop

    def display_items_for_sale(self):
        items = self.controller.get_items_for_sale()
        for i, item in enumerate(items, start=1):
            print(f"{i}. Item: {item.name}, Preco: {self.controller.evaluate_item_price(item)}")

    def display_options(self):
        PrintUtils.print_centered("Loja de Itens\n")
        PrintUtils.print_separator_line()
        print("1. Comprar")
        print("2. Vender")
        print("3. Abrir Inventario")
        print("4. Abrir Journal")
        print("5. Salvar jogo")
        print("6. Sair")


    def handle_input(self):
        while self.is_running :
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                self.display_items_for_sale()
                item_number = int(input("\nDigite o numero do item que voce quer comprar (0 para voltar): "))
                
                if item_number == 0:
                   pass

                items = self.controller.get_items_for_sale()
                if 1 <= item_number <= len(items):
                    item_to_buy = items[item_number - 1]
                    self.controller.buy_item(item_to_buy)
                else:
                    print("Numero de item invalido")
            elif input_value == "2":
                player_items = PlayerController.get_player().inventory.items
                for i, item in enumerate(player_items, start=1):
                    price = self.controller.evaluate_item_price(item)
                    print(f"{i}. Item: {item.name}, Preco: {price}")
                item_number = int(input("\nDigite o numero do item que voce quer vender: "))
                if 1 <= item_number <= len(player_items):
                    item_to_sell = player_items[item_number - 1]
                    self.controller.sell_item(item_to_sell)
                else:
                    print("Numero de item invalido\n")  
            elif input_value == "3":
                self.controller.open_inventory()
            elif input_value == "4":
                self.controller.open_journal()
            elif input_value == "5":
                self.stop_view()
                PlayerController.save_player_state()
            elif input_value == "6":
                self.stop_view()
                LocationService.leave(self.previous_structure_view)
                break
            else:
                print("Opcao invalida.")


    def init_view(self):
        self.is_running = True
        self.handle_input()


    def stop_view(self):
        self.is_running = False
