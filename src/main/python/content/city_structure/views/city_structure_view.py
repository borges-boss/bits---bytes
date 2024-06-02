from content.player.controllers.player_controller import PlayerController
from content.inn.views.inn_view import InnView
from python.content.shop.views.shop_view import ShopView
from python.content.tavern.views.tavern_view import TavernView
from python.services.location_service import LocationService
from utils.print_utils import PrintUtils
from utils.console_utils import ConsoleUtils

class CityStructureView:

    def __init__(self,previous_structure_view):
      self.is_running = True
      self.previous_structure_view = previous_structure_view
     
    def display_options(self):
        PrintUtils.print_centered(f'Cidade de {PlayerController.get_player().city}\n')
        PrintUtils.print_separator_line()
        print("1. Visitar Inn")
        print("2. Visitar Shop")
        print("3. Visitar Tavern")
        print("4. Sair da  cidade")


    def handle_input(self):
        while self.is_running:
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                InnView(self).init_view()
            elif input_value == "2":
                ShopView(self).init_view()
            elif input_value == "3":
                TavernView(self).init_view()
            elif input_value == "4":
                self.stop_view()
                LocationService.leave(self.previous_structure_view)
            else:
                print("Invalid option.")

    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_view(self):
        self.is_running = False