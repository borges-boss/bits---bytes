from content.journal.models.journal_model import JournalModel
from content.journal.views.journal_view import JournalView
from utils.print_utils import PrintUtils


class JournalController:
    def __init__(self):
        self.model = JournalModel()
        self.view = JournalView()

    def show_active_quests(self):
        active_quests = self.model.get_all_active_quests()
        print("Active Quests\n")
        self.view.show_quests(active_quests)

    def show_completed_quests(self):
        completed_quests = self.model.get_all_completed_quests()
        print("Completed Quests\n")
        self.view.show_quests(completed_quests)

    def complete_quest(self, quest_name):
        quest = next((q for q in self.model.get_all_active_quests() if q.name == quest_name), None)
        if quest is not None:
            self.model.complete_quest(quest)
            print(f"Quest '{quest_name}' has been marked as completed.")
        else:
            print(f"No active quest found with name '{quest_name}'.")


    def show_my_quests(self):
        PrintUtils.print_centered("Diario de Missões\n")
        PrintUtils.print_separator_line()
        self.show_active_quests()
        PrintUtils.print_separator_line()
        self.show_completed_quests()