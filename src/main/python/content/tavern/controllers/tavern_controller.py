from content.tavern.views.tavern_view import TavernView
from content.tavern.models.tavern_model import TavernModel
from classes.player import Player

class TavernController:

    def __init__(self,city_name):
        self.city_name = city_name
        self.model = TavernModel()

    def get_taverns_by_city(self):
        return self.model.get_taverns_by_city(self.city_name)

    def list_available_quests(self):
        return self.list_available_quests(self.city_name) 
    

    def explore(self):
        self.model.explore()

    def open_inventory(self):
        self.model.open_inventory()

    def open_journal(self):
        self.model.open_journal()

    def leave(self):
        self.model.leave()

    
