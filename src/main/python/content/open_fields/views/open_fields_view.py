from content.open_fields.controllers.open_fields_controller import OpenFieldsController
from content.player.controllers.player_controller import PlayerController
from constants.constants import STRUCTURE_TYPE_DUNGEON
from content.dungeon.views.dungeon_view import DungeonView
from content.cave.views.cave_view import CaveView
from services.location_service import LocationService
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class OpenFieldsView:
    def __init__(self, open_field):
        self.is_running = True
        self.controller = OpenFieldsController()
        self.open_field = open_field

    def display_options(self):
        PrintUtils.print_centered(f"Voce esta em um campo aberto fora da cidade de {PlayerController.get_player().city}\n")
        PrintUtils.print_separator_line()
        print("1. Explore")
        print("2. Abrir Inventario")
        print("3. Abrir Journal")
        print("4. Viajar")

        if self.open_field.structures:
            print("\nEstruturas:")
            for i, structure in enumerate(self.open_field.structures, start=5):
              difficulty = 'Facil' if structure.dificulty == 1 else 'Normal' if structure.dificulty == 2 else 'Dificil'
              print(f"{i}. Explore {structure.type.capitalize()} (Dificuldade: {difficulty})")

    def handle_input(self):
        while True:
            ConsoleUtils.clear_terminal()
            self.display_options()
            input_value = input("Choose an option: ")
            if input_value == "1":
                LocationService.explore(self.open_field,self)
            elif input_value == "2":
                self.controller.open_inventory()
            elif input_value == "3":
                self.controller.open_journal()
            elif input_value == "4":
                self.stop_view()
                LocationService.travel()
                break
            elif int(input_value) >= 5 and int(input_value) <= len(self.open_field.structures) + 4:
                structure = self.open_field.structures[int(input_value) - 5]
                self.stop_view()

                if structure.type == STRUCTURE_TYPE_DUNGEON:
                    DungeonView(self,structure).init_view()
                else:
                    CaveView(self,structure).init_view()
            else:
                print("Opcao invalida.")

    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_view(self):
        self.is_running = False