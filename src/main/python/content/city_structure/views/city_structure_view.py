from content.player.controllers.player_controller import PlayerController
from content.inn.views.inn_view import InnView
from constants.constants import STRUCTURE_TYPE_INN, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from content.shop.views.shop_view import ShopView
from content.tavern.views.tavern_view import TavernView
from content.open_fields.views.open_fields_view import OpenFieldsView
from services.location_service import LocationService
from utils.print_utils import PrintUtils
from utils.console_utils import ConsoleUtils

class CityStructureView:

    def __init__(self,city_open_field, structures):
      self.is_running = True
      self.previous_structure_view = OpenFieldsView(city_open_field)
      self.structures = structures
     
    def display_options(self):
        PrintUtils.print_centered(f'Cidade de {PlayerController.get_player().city}\n')
        PrintUtils.print_separator_line()
        print("1. Visitar Inn")
        print("2. Visitar Shop")
        print("3. Visitar Tavern")
        print("4. Sair da cidade")


    def handle_input(self):
        while self.is_running:
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                inn = next((s for s in self.structures if s.type == STRUCTURE_TYPE_INN), None)
                if inn is not None:
                    PlayerController.get_player().location = inn
                    self.stop_view()
                    InnView(self, inn).init_view()
                else:
                    print("\nNenhum Inn nessa cidade.")
            elif input_value == "2":
                shop = next((s for s in self.structures if s.type == STRUCTURE_TYPE_SHOP), None)
                if shop is not None:
                    PlayerController.get_player().location = shop
                    self.stop_view()
                    ShopView(self, shop).init_view()
                else:
                    print("\nNenhuma loja nessa cidade.")
            elif input_value == "3":
                tavern = next((s for s in self.structures if s.type == STRUCTURE_TYPE_TAVERN), None)
                if tavern is not None:
                    PlayerController.get_player().location = tavern
                    self.stop_view()
                    TavernView(self, tavern).init_view()
                else:
                    print("\nNenhuma taverna nessa cidade.")
            elif input_value == "4":
                self.stop_view()
                LocationService.leave(self.previous_structure_view)
            else:
                print("Opcao invalida.")

    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_view(self):
        self.is_running = False