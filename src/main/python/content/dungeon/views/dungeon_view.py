from content.dungeon.controllers.dungeon_controller import DungeonController
from content.player.controllers.player_controller import PlayerController
from utils.console_utils import ConsoleUtils
from services.location_service import LocationService
from utils.print_utils import PrintUtils


class DungeonView:
    def __init__(self,previous_structure_view,dungeon):
        self.controller = DungeonController()
        self.previous_structure_view = previous_structure_view
        self.is_running = True
        self.dungeon = dungeon

    def display_options(self):
        PrintUtils.print_centered("Voce está explorando uma dangeon\n")
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
                self.stop_view()
                LocationService.explore(self.dungeon, self)
            elif input_value == "2":
                self.controller.open_inventory()
            elif input_value == "3":
                self.controller.open_journal()
            elif input_value == "4":
                PlayerController.save_player_state()
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