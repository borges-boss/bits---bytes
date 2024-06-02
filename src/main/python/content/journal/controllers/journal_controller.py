from content.journal.models.journal_model import JournalModel
from content.journal.views.journal_view import JournalView
from utils.print_utils import PrintUtils


class JournalController:
    def __init__(self):
        self.model = JournalModel()
        self.view = JournalView()

    def get_active_quests(self):
        return self.model.get_all_active_quests()

    def get_completed_quests(self):
        return self.model.get_all_completed_quests()

    def complete_quest(self, quest_name):
        quest = next((q for q in self.model.get_all_active_quests() if q.name == quest_name), None)
        if quest is not None:
            self.model.complete_quest(quest)
            print(f"Quest '{quest_name}' foi completa!.")
        else:
            print(f"Nenhuma quest ativa encontrada com o nome '{quest_name}'.")
