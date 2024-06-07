import datetime
from base.journal import Journal
from base.wallet import Wallet
from classes.inventory import Inventory
from classes.player import Player
from services.data_mapper import DataMapper
from services.data_store import DataStore


class GameSaveModel:

    def __init__(self):
        self.datastore = DataStore()

    def parse_player_info(self, player_info) -> Player:
        wallet = Wallet(player_info['wallet']['coins'])

        inventory = Inventory([DataMapper.map_dict_to_item(item) for item in player_info['inventory']['items']], player_info['inventory']['max_weight'])

        equipped_item = DataMapper.map_dict_to_item(player_info['equipped_item'])

        equipped_armor = [DataMapper.map_dict_to_item(item) for item in player_info['equipped_armor']]

        journal = Journal([DataMapper.map_dict_to_quest(quest_data) for quest_data in player_info['journal']['quests']])

        location = DataMapper.map_structures_to_class_object(player_info['location'])
            
        abilities = [DataMapper.map_dict_to_ability(ability)
                     for ability in player_info['abilities']]

        player = Player(player_info['health'], player_info['mana'],player_info['stamina'], player_info['player_id'], player_info['name'], player_info['race'],
                        player_info['game_class'], abilities, player_info['level'], player_info['xp'], wallet, inventory,
                        equipped_item, equipped_armor, journal, location, player_info['city'])
        return player

    def get_saves(self):
        return self.datastore.find_saves()
    
    def get_player_info(self) -> Player:
        saves = self.datastore.find_saves()

        if not saves: 
            return None
        
        most_recent_save = max(saves, key=lambda save: datetime.datetime.strptime(save['last_save'], "%Y-%m-%dT%H:%M:%S.%f"))
        return self.parse_player_info(most_recent_save['player_info'])

    def save_game(self,player):
        self.datastore.save_game(player)