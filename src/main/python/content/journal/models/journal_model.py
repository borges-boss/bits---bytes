from services.data_store import DataStore

class JournalModel:

    def __init__(self):
        self.datastore = DataStore()


    def get_all_active_quests(self):
        return self.datastore.find_active_quests()
    
    def get_all_completed_quests(self):
        return self.datastore.find_completed_quests()

    def complete_quest(self,quest):
        self.datastore.update_quest_status(quest.name, True)



