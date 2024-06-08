from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView

class CaveModel:

    def open_inventory(self, player):
        view = InventoryView(player)
        view.init_view()

    def open_journal(self):
        view = JournalView()
        view.init_view()