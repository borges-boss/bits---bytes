from services.data_store import DataStore

class TavernModel:
    
    def __init__(self):
        self.datastore = DataStore()


    def get_quests(self,city):
        return self.datastore.find_quests_by_city(city)
    
    def get_taverns_by_city(self,city):
        return self.datastore.find_taverns_by_city(city)

