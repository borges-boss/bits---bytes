import random
import time
from constants.constants import ITEM_RARITY_COMMON, ITEM_RARITY_EPIC, ITEM_RARITY_LEGENDARY, ITEM_RARITY_RARE
from content.player.controllers.player_controller import PlayerController
from content.battle.views.battle_view import BattleView
from services.monster_service import MonsterService
from services.item_service import ItemService
from services.data_store import DataStore
from utils.print_utils import PrintUtils
from utils.console_utils import ConsoleUtils


class LocationService:

    @staticmethod
    def explore(current_structure, current_view):
        difficulty = current_structure.dificulty
        monster_probabilities = {1: 0.2, 2: 0.35, 3: 0.5, 4: 0.7}
        loot_probabilities = {1: 0.35, 2: 0.25, 3: 0.15, 4: 0.08}

        ConsoleUtils.clear_terminal()
        PrintUtils.print_dot_loading_animation("Explorando")
        ConsoleUtils.clear_terminal()

        if random.random() < monster_probabilities[difficulty]:
            print("Voce encontrou um monstro!")
            BattleView(MonsterService.spawn_monster_by_difficulty(difficulty),current_structure).init_view()
        elif random.random() < loot_probabilities[difficulty]:
            datastore = DataStore()
            rarity = None
            if difficulty == 1:  # Fácil
                # 80% de chance para comum, 20% de chance para raro
                rarity = ITEM_RARITY_COMMON if random.random() < 0.8 else ITEM_RARITY_RARE
            elif difficulty == 2:  # Normal
                # 70% de chance para comum, 25% de chance para raro, 5% de chance para épico
                rand_num = random.random()
                if rand_num < 0.7:
                    rarity = ITEM_RARITY_COMMON
                elif rand_num < 0.95:
                    rarity = ITEM_RARITY_RARE
                else:
                    rarity = ITEM_RARITY_EPIC
            elif difficulty == 3:  # Difícil
                # 50% de chance para comum, 30% de chance para raro, 15% de chance para épico, 5% de chance para lendário
                rand_num = random.random()
                if rand_num < 0.5:
                    rarity = ITEM_RARITY_COMMON
                elif rand_num < 0.8:
                    rarity = ITEM_RARITY_RARE
                elif rand_num < 0.95:
                    rarity = ITEM_RARITY_EPIC
                else:
                    rarity = ITEM_RARITY_LEGENDARY

        items_by_rarity = datastore.find_items_by_rarity(rarity)
        if items_by_rarity:
            item = random.choice(items_by_rarity)
            print(f"Voce encontrou {item['_name']}!")
            PlayerController.get_player().inventory.add_item(ItemService.map_to_item(item))
            time.sleep(3)
        else:
            PrintUtils.print_slowly("Voce explorou o local mas não encontrou nada. Melhor continuar andando...")
            time.sleep(3)
        
        ConsoleUtils.clear_terminal()
        current_view.init_view()

    @staticmethod
    def travel():
        from content.city_structure.views.city_structure_view import CityStructureView
        from content.open_fields.controllers.open_fields_controller import OpenFieldsController

        datastore = DataStore()
        open_field_controller = OpenFieldsController()
        cities = datastore.find_cities()
        
        print("Escolha uma cidade:")
        for i, city in enumerate(cities, start=1):
            print(f"{i}. {city.name}")

        while True:
            try:
                city_number = int(input("Digite o numero da cidade que voce quer viajar: "))
                if 1 <= city_number <= len(cities):
                    break
                else:
                    print("Numero da cidade invalido. Por favor tente de novo.")
            except ValueError:
                print("Input invalido. Por favor digite apenas numeros.")

        chosen_city = cities[city_number - 1]
        open_fields_in_city = open_field_controller.find_open_fields_by_city(chosen_city.name)
        
        city_view = CityStructureView(open_fields_in_city[0], chosen_city.structures)
        ConsoleUtils.clear_terminal()
        PrintUtils.print_dot_loading_animation("Viajando")
        PlayerController.get_player().city = chosen_city.name
        city_view.init_view()


    @staticmethod
    def leave(structure_view_to_go_back_to):
        structure_view_to_go_back_to.init_view()