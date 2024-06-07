from content.cave.controllers.cave_controller import CaveController
from content.player.controllers.player_controller import PlayerController
from services.location_service import LocationService
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class CaveView:

    def __init__(self, previous_structure_view, cave):
        self.controller = CaveController()
        self.previous_structure_view = previous_structure_view
        self.is_running = True
        self.cave = cave
        self.player = PlayerController.get_player()
        self.player.location = cave

    def display_options(self):
        PrintUtils.print_centered("Voce está explorando uma caverna\n")
        PrintUtils.print_separator_line()
        print("1. Explorar")
        print("2. Abrir Inventario")
        print("3. Abrir Journal")
        print("4. Salvar jogo")
        print("5. Sair")

    def handle_input(self):
        while self.is_running:
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Escolha uma opção: ")
            if input_value == "1":
                LocationService.explore(self.cave,self,self.player)
            elif input_value == "2":
                self.controller.open_inventory()
            elif input_value == "3":
                self.controller.open_journal()
            elif input_value == "4":
                PlayerController.save_player_state(self.player)
            elif input_value == "5":
                self.stop_view()
                LocationService.leave(self.previous_structure_view)
                break
            else:
                print("Opcao invalida")

    def init_view(self):
        self.is_running = True
        self.handle_input()


    def stop_view(self):
        self.is_running = False
