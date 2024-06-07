from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView

class DungeonModel:

    def open_inventory(self):
        view = InventoryView()
        view.init_view()

    def open_journal(self):
        view = JournalView()
        view.init_view()