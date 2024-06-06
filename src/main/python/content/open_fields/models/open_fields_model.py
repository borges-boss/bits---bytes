from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView
from services.data_store import DataStore

class OpenFieldsModel:

    def __init__(self):
        self.datastore = DataStore()
 
    def open_inventory(self):
        view = InventoryView()
        view.init_view()

    def open_journal(self):
        view = JournalView()
        view.init_view()

    def find_open_fields_by_city(self, city):
        return self.datastore.find_open_fields_by_city(city)


    

