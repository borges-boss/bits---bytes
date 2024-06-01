from content.tavern.views.tavern_view import TavernView
from content.tavern.models.tavern_model import TavernModel
from classes.player import Player

class TavernController:

    def __init__(self,city_name):
        self.city_name = city_name
        self.model = TavernModel()

    def list_available_quests(self):
        taverns = self.model.get_taverns_by_city(self.city_name)
        if len(taverns) > 0:
            view  = TavernView(taverns[0])
            view.list_quests(taverns[0].tavern_keeper_dialog)
        return taverns
    

    def enter_tavern(self, player:Player):
        taverns = self.list_available_quests(self.city_name) 

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
            player.journal.add_quest(quest_to_add)
            print(f"Quest '{quest_to_add.name}' foi adicionada ao seu journal.")
        else:
            print("Nenhuma taverna disponivel nessa cidade")

