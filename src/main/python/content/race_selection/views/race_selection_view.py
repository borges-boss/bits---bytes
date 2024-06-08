from classes.player import Player
from constants.constants import  RACE_TYPE_DWARF, RACE_TYPE_HALF_ELF, RACE_TYPE_HUMAN, RACE_TYPE_LIZARDFOLK, RACE_TYPE_ORC, RACE_TYPE_HIGH_ELF
from content.player.models.player_model import PlayerModel
from content.class_selection.views.class_selection_view import ClassSelectionView
from content.player.controllers.player_controller import PlayerController
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class RaceSelectionView:


    def __init__(self) -> None:
        self.available_races = [RACE_TYPE_HUMAN, RACE_TYPE_HIGH_ELF, RACE_TYPE_DWARF, RACE_TYPE_HALF_ELF, RACE_TYPE_LIZARDFOLK, RACE_TYPE_ORC]
        self.player_model = PlayerModel()
        self.is_running = True
        self.player = PlayerController.get_player()

    def select_race(self):
        PrintUtils.print_centered("Available races:")
        print("\n")
        PrintUtils.print_separator_line()

        for i, race_type in enumerate(self.available_races, start=1):
            temp_player = Player(race=race_type)

            base_health = self.player_model.get_base_health(temp_player)
            base_mana = self.player_model.get_base_mana(temp_player)
            base_stamina = self.player_model.get_base_stamina(temp_player)
            base_damage = self.player_model.get_base_damage(temp_player)
            base_defence = self.player_model.get_base_defence(temp_player)

            print(f"{i}. {race_type}")
            print(f"   Saude: {base_health}")
            print(f"   Mana: {base_mana}")
            print(f"   Stamina: {base_stamina}")
            print(f"   Dano: {base_damage}")
            print(f"   Defesa: {base_defence}\n")

        while self.is_running:
            try:
                race_choice = int(input("Digite o numero da raca que voce deseja escolher: "))
                if 1 <= race_choice <= len(self.available_races):
                    chosen_race = self.available_races[race_choice - 1]
                    print(f"Voce escolheu {chosen_race}.")
                    confirm = input("Voce tem certeza que quer escolher essa raca? (s/n): ")

                    if confirm.lower() == 's':
                        self.player.race = chosen_race
                        PlayerController.silent_save(self.player)
                        self.stop_view()
                        ConsoleUtils.clear_terminal()
                        ClassSelectionView().init_view()
                    else:
                        print("Ok, vamos tentar novamente.")
                else:
                    print("Escolha invalida. Por favor digite um numero correspondente as racas listadas acima.")
            except ValueError:
                print("Input invalido. Por favor digite apenas numeros")


    def init_view(self):
        self.is_running = True
        self.select_race()


    def stop_view(self):
        self.is_running = False