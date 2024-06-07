from content.inn.models.inn_model import InnModel
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView

class InnController:
    def __init__(self, inn):
        self.model = InnModel(inn)

    def rest(self, player):
        self.model.rest(player)

    def open_inventory(self):
        view = InventoryView()
        view.init_view()

    def open_journal(self):
        view = JournalView()
        view.init_view()