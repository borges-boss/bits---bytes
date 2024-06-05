import time
from content.tavern.controllers.tavern_controller import TavernController
from content.player.controllers.player_controller import PlayerController
from services.location_service import LocationService
from utils.print_utils import PrintUtils
from utils.console_utils import ConsoleUtils
from constants.constants import REWARD_TYPE_ITEM

class TavernView:

    def __init__(self, previous_structure_view,tavern):
        self.controller = TavernController()
        self.previous_structure_view = previous_structure_view
        self.is_running  = True
        self.tavern = tavern
    
    def list_available_quests(self):
        taverns = self.controller.get_taverns_by_city()
        if len(taverns) > 0:
            self.list_quests(taverns[0].tavern_keeper_dialog)
            self.input_quest()
        return taverns

    def list_quests(self,tavern_keeper_dialog: str, tavern):
        PrintUtils.print_slowly(tavern.tavern_keeper.name+" o "+tavern.tavern_keeper.role+" diz: "+tavern_keeper_dialog,0.05)
        print("\n")
        PrintUtils.print_slowly("Seja bem vindo a taverna "+tavern.name+"\n",0.05)
        print("Missões Disponiveis\n")
        PrintUtils.print_separator_line()
        
        for quest in tavern.quests:
            self.display_quest_info(quest)
            PrintUtils.print_separator_line()


    def display_quest_info(self,quest):
        status = "Completed" if quest.is_completed else "Not Completed"
        if quest.reward_type == REWARD_TYPE_ITEM:
            print(f'Quest Name: {quest.name}\nDescription: {quest.description}\nReward: {quest.reward.name}\nStatus: {status}')
        else:
            print(f'Quest Name: {quest.name}\nDescription: {quest.description}\nReward: {quest.reward} coins\nStatus: {status}')


    def input_quest(self, player):
        taverns = self.controller.get_taverns_by_city()

        if taverns:
            print("Digite o numero da quest que voce quer adicionar ao seu journal: ")
            for i, quest in enumerate(taverns[0].quests, start=1):
                print(f"{i}. {quest.name}")

            while True:
                try:
                    quest_number = int(input())
                    if 1 <= quest_number <= len(taverns[0].quests):
                        break
                    else:
                        print("Numero invalido, por favor tente de novo")
                except ValueError:
                    print("Input invalido, por favor so digite numeros")

            quest_to_add = taverns[0].quests[quest_number - 1]

            if any(quest.name == quest_to_add.name for quest in player.journal.quests):
                print(f"Quest '{quest_to_add.name}' ja esta no seu journal.")
            else:
                player.journal.add_quest(quest_to_add)
                print(f"Quest '{quest_to_add.name}' foi adicionada ao seu journal.")
        else:
            print("Nenhuma taverna disponivel nessa cidade")

        time.sleep(3)
        ConsoleUtils.clear_terminal()
        self.init_view()




    def display_options(self):
        PrintUtils.print_centered("Taverna\n")
        PrintUtils.print_separator_line()
        print("1. Ver quests disponiveis")
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
                self.list_available_quests()
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
