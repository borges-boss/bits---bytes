

from content.cave.models.cave_model import CaveModel
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView


class CaveController:
    def __init__(self):
        self.model = CaveModel()

    def explore(self):
        self.model.explore()

    def open_inventory(self):
        self.model.open_inventory()

    def open_journal(self):
        self.model.open_journal()

    def leave(self):
        self.model.leave()