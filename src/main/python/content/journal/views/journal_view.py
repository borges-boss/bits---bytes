import keyboard
from content.journal.controllers.journal_controller import JournalController
from utils.print_utils import PrintUtils


class JournalView:

    def __init__(self):
        self.controller = JournalController()


    def show_quests(self, quests):
        for quest in quests:
            print(f"Name: {quest.name}\nDescription: {quest.description}\n")

    def show_active_quests(self,active_quests):
        print("Active Quests\n")
        self.show_quests(active_quests)

    def show_completed_quests(self, completed_quests):
        print("Completed Quests\n")
        self.show_quests(completed_quests)

    def show_my_quests(self):
        PrintUtils.print_centered("Diario de Missões\n")
        PrintUtils.print_separator_line()
        self.show_active_quests(self.controller.get_active_quests())
        PrintUtils.print_separator_line()
        self.show_completed_quests(self.controller.get_completed_quests())


    def init_view(self):
        self.show_my_quests()
        print("q para fechar")
        keyboard.wait("q")