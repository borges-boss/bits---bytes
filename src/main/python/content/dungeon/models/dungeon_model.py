from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView

class DungeonModel:

    def explore(self):
        pass 

    def open_inventory(self):
        view = InventoryView()
        view.display_items()

    def open_journal(self):
        view = JournalView()
        view.show_my_quests()

    def leave(self):
       pass