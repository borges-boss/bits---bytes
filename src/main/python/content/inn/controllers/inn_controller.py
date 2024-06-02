from content.inn.models.inn_model import InnModel
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView

class InnController:
    def __init__(self, inn):
        self.model = InnModel(inn)

    def rest(self):
        self.model.rest()

    def open_inventory(self):
        view = InventoryView()
        view.display_items()

    def open_journal(self):
        view = JournalView()
        view.show_my_quests()

    def leave(self, previous_structure_view):
        self.model.leave()