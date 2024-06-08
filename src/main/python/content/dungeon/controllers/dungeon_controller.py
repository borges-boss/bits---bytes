from content.dungeon.models.dungeon_model import DungeonModel
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView


class DungeonController:
    def __init__(self):
        self.model = DungeonModel()

    def open_inventory(self, player):
        self.model.open_inventory(player)

    def open_journal(self):
        self.model.open_journal()