import random
import time
from classes.monster import Monster
from content.player.controllers.player_controller import PlayerController
from content.inventory.views.inventory_view import InventoryView
from constants.constants import ABILITY_TYPE_PHYSICAL, ABILITY_TYPE_MAGIC
from classes.player import Player
from services.monster_service import MonsterService
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
        self.player = PlayerController.get_player()

    def display_abilities(self):
        print("\nAbilities:")
        for i, ability in enumerate(self.player.abilities, start=1):
            cost_type = 'Stamina' if ability.type == ABILITY_TYPE_PHYSICAL else 'Mana'
            if ability.type == ABILITY_TYPE_PHYSICAL or ability.type == ABILITY_TYPE_MAGIC:
                print(f"{i}. {ability.name} - {ability.description} (Dano: {ability.value}, Custo: {ability.ability_cost} {cost_type})")
            else:
                print(f"{i}. {ability.name} - {ability.description} (Efeito: {ability.value}, Custo: {ability.ability_cost} {cost_type})")

    def refresh_hud(self):
            ConsoleUtils.clear_terminal()
            PlayerController.display_player_hud(self.player)
            MonsterService.display_monster_hud(self.target)

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
            self.refresh_hud()
            self.display_options()
            if self.player_turn: 
                input_value = input("Escolha uma opcao: ")
                if input_value == "1":
                    self.display_abilities()
                    ability_choice = input("Escolha uma abilidade: ")
                    try:
                        chosen_ability = self.player.abilities[int(ability_choice) - 1]
                        ability_result_entity = PlayerController.useAbility(chosen_ability, self.target,self.player)

                        if isinstance(ability_result_entity,Player):
                            self.player = ability_result_entity
                        else:
                            self.target = ability_result_entity

                        self.player_turn = False  
                        time.sleep(3)
                        self.refresh_hud()
                        self.display_options()
                    except (IndexError, ValueError):
                        print("Abilidade invalida.")

                elif input_value == "2":
                    self.is_player_defending = True
                    self.player_turn = False  

                elif input_value == "3":
                    InventoryView().init_view()

                elif input_value == "4":
                    ConsoleUtils.clear_terminal()
                    if random.random() < 0.50:  # 25% de change de falhar
                        print("Você tentou fugir da batalha, mas falhou...")
                        self.player_turn = False
                    else:
                        print("Você fugiu da batalha como um covarde, mas pelo menos ainda está vivo...")
                        PlayerController.init_player_battle_attributes(self.player)  # Resetar atributos do player depois da batalha
                        time.sleep(4)
                        self.stop_view()
                        self.out_of_battle_view.init_view()
                else:
                    print("Opcao invalida")

            else:
                print(f"E a vez do {self.target.name} (Level:{self.target.level})")
                PrintUtils.print_dot_loading_animation(f"{self.target.name} esta prestes a atacar")

                initial_defence = self.player.defence

                if self.is_player_defending:
                    self.player.defence = self.player.defence * 1.5

                if self.target.abilities: 
                    chosen_ability = random.choice(self.target.abilities)

                    result_monster_entity_ability = self.target.useAbility(chosen_ability, self.player)
                    if isinstance(result_monster_entity_ability, Monster):
                        self.target = result_monster_entity_ability
                    else:
                        self.player = result_monster_entity_ability 

                    time.sleep(3)
                    
                    if self.is_player_defending:
                        #Resetar atributo de defesa do player depois de defender
                        self.player.defence = initial_defence
                        self.is_player_defending = False

                    time.sleep(2)
                self.player_turn = True  

            if self.player.health <= 0:
                ConsoleUtils.clear_terminal()
                print("Voce foi derrotado...")
                PrintUtils.print_slowly(f"\nDe alguma forma voce conseguiu sobreviver e se arrastar para um local seguro. Mas cuidado porque pode não haver uma proxima vez...")
                time.sleep(3)
                PlayerController.init_player_battle_attributes(self.player) # Resetar atributos do player depois da batalha
                self.player.health = PlayerController.get_player_max_health() * 0.25  #Se o player for derrotado restaure 25% da vida maxima dele
                self.player.wallet.add_coins(1)
                PlayerController.silent_save(self.player)
                self.stop_view()
                self.out_of_battle_view.init_view()

            elif self.target.health <= 0:
                print(f"\nVoce derrotou o {self.target.name}!")
                self.player.wallet.add_coins(2)
                loot = LootService.get_random_loot_from_monster(self.target)

                if loot is not None:
                 print(f"\nVoce ganhou {loot.name} como recompensa")
                 self.player.inventory.add_item(loot)
                 PlayerController.silent_save(self.player)

                time.sleep(4)
                xp_amount = (self.target.level * 10) + self.player.xp
                print(f"\nVoce ganhou {xp_amount} de xp")
                PlayerController.add_exp(xp_amount)
                PlayerController.init_player_battle_attributes(self.player) # Resetar atributos do player depois da batalha
                
                time.sleep(4)
                self.stop_view()
                self.out_of_battle_view.init_view()


    def init_view(self):
        self.is_running = True
        self.handle_input()

    def stop_view(self):
        self.is_running = False