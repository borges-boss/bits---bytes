import random
import time
from classes.monster import Monster
from content.player.controllers.player_controller import PlayerController
from content.inventory.views.inventory_view import InventoryView
from services.loot_service import LootService
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class BattleView:

    def __init__(self, target: Monster, out_of_battle_view):
        self.target = target
        self.out_of_battle_view = out_of_battle_view
        self.is_running = True
        self.player_turn = True 
        self.is_player_defending = False

    def display_options(self):
        PrintUtils.print_centered(f"Voce esta em batalha contra {self.target.name} de nivel {self.target.level}\n")
        PrintUtils.print_separator_line()
        if self.player_turn: 
            print("1. Ataque")
            print("2. Defesa")
            print("3. Abrir inventario")
            print("4. Fugir")

    def handle_input(self):
        while self.is_running:
            PlayerController.display_player_hud()
            self.display_options()
            if self.player_turn: 
                input_value = input("Escolha uma opcao: ")
                if input_value == "1":
                    self.display_abilities()
                    ability_choice = input("Escolha uma abilidade: ")
                    try:
                        chosen_ability = PlayerController.get_player().abilities[int(ability_choice) - 1]
                        PlayerController.useAbility(chosen_ability, self.target)
                        self.player_turn = False  
                    except (IndexError, ValueError):
                        print("Abilidade invalida.")
                elif input_value == "2":
                    self.is_player_defending = True
                    self.player_turn = False  
                elif input_value == "3":
                    InventoryView().init_view()
                elif input_value == "4":
                    ConsoleUtils.clear_terminal()
                    print("Voce fugiu da batalha como um covarde, mas pelo menos ainda esta vivo...")
                    self.out_of_battle_view.init_view()
                else:
                    print("Opcao invalida")
            else:
                print(f"E a vez do {self.target.name} (Level:{self.target.level})")
                PrintUtils.print_dot_loading_animation(f"{self.target.name} esta prestes a atacar")

                if self.target.abilities: 
                    chosen_ability = random.choice(self.target.abilities)
                    if self.is_player_defending:
                        initial_defence = PlayerController.get_player().defence
                        PlayerController.get_player().defence = initial_defence * 2
                        self.target.useAbility(chosen_ability, PlayerController.get_player()) 
                        PlayerController.get_player().defence = initial_defence
                    else: 
                        self.target.useAbility(chosen_ability, PlayerController.get_player()) 

                    time.sleep(2)
                self.player_turn = True  

            if PlayerController.get_player().health <= 0:
                ConsoleUtils.clear_terminal()
                print("Voce foi derrotado...")
                PrintUtils.print_slowly(f"\nDe alguma forma voce conseguiu sobreviver e se arrastar para um local seguro. Mas cuidado porque pode não haver uma proxima vez...")
                time.sleep(3)
                self.stop_view()
                self.out_of_battle_view.init_view()
            elif self.target.health <= 0:
                print(f"\nVoce derrotou o {self.target.name}!")
                loot = LootService.get_random_loot_from_monster(self.target)
                if loot is not None:
                 PlayerController.get_player().inventory.add_item(loot)

                xp_amount = (self.target.level * 10) + PlayerController.get_player().xp
                print(f"\nVoce ganhou {xp_amount} de xp")
                PlayerController.get_player().xp(xp_amount)
                self.stop_view()
                self.out_of_battle_view.init_view()


    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_view(self):
        self.is_running = False