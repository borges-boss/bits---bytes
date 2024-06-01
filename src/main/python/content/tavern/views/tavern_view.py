from classes.tavern import Tavern
from utils.print_utils import PrintUtils
from constants.constants import REWARD_TYPE_ITEM

class TavernView:

    def __init__(self,tavern:Tavern):
        self.tavern = tavern

    def list_quests(self,tavern_keeper_dialog: str):
        PrintUtils.print_slowly(self.tavern.tavern_keeper.name+" o "+self.tavern.tavern_keeper.role+" diz: "+tavern_keeper_dialog,0.05)
        print("\n")
        PrintUtils.print_slowly("Seja bem vindo a taverna "+self.tavern.name+"\n",0.05)
        print("Missões Disponiveis\n")
        PrintUtils.print_separator_line()
        
        for quest in self.tavern.quests:
            self.display_quest_info(quest)
            PrintUtils.print_separator_line()


    def display_quest_info(self,quest):
        status = "Completed" if quest.is_completed else "Not Completed"
        if quest.reward_type == REWARD_TYPE_ITEM:
            print(f'Quest Name: {quest.name}\nDescription: {quest.description}\nReward: {quest.reward.name}\nStatus: {status}')
        else:
            print(f'Quest Name: {quest.name}\nDescription: {quest.description}\nReward: {quest.reward} coins\nStatus: {status}')
