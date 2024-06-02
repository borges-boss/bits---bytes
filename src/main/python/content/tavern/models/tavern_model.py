from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView
from services.data_store import DataStore

class TavernModel:
    
    def __init__(self):
        self.datastore = DataStore()


    def get_quests(self,city):
        return self.datastore.find_quests_by_city(city)
    
    def get_taverns_by_city(self,city):
        return self.datastore.find_taverns_by_city(city)

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
