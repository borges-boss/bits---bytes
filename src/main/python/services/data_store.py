import datetime
import os
from base.item import Item
from base.quest import Quest
from classes.npc import Npc
from classes.tavern import Tavern
from typing import List
from classes.inn import Inn
from classes.shop import Shop
from base.enchantment import Enchantment
from classes.cave import Cave
from classes.city import City
from classes.consumable_item import ConsumableItem
from classes.damage_item import DamageItem
from classes.dungeon import Dungeon
from classes.monster import Monster
from classes.open_fields import OpenFields
from classes.wearable_item import WearableItem
from constants.constants import ITEM_TYPE_CONSUMABLE, ITEM_TYPE_DAMAGE, ITEM_TYPE_WEARABLE, STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from services.data_mapper import DataMapper
from services.json_file_proc import JsonFileProcessor

class DataStore:
    def __init__(self):
      self.json_file_processor = JsonFileProcessor()


    def get_path(self,file_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        file_path = os.path.join(base_dir, 'datastore', file_name)
        return file_path
    
    def read_file_content(self,file_name):
        return self.json_file_processor.read_file_contents(self.get_path(file_name))
    

    def find_data_by_key(self, key):
        data = self.read_file_content("data.json")
        if data and key in data:
            value = data[key]
            return value if isinstance(value, list) else [value]
        else:
            return []
        

    def find_save_by_key(self, key):
        data = self.read_file_content("saves.json")
        if data and key in data:
            value = data[key]
            return value if isinstance(value, list) else [value]
        else:
            return []
        
    
    def find_quests_by_city(self, city):
        data = self.read_file_content("quests.json")
        quests = []
        for quest_data in data['quests']:
            if quest_data['city'] == city:            
                quest = Quest(DataMapper.map_dict_to_quest(quest_data))
                quests.append(quest)

        return quests
    


    def find_active_quests(self):
        data = self.read_file_content("saves.json")
        active_quests = []
        for save in data['saves']:
            for quest in save['player_info']['journal']['quests']:
                if not quest['is_completed']:
                    active_quests.append(DataMapper.map_dict_to_quest(quest))
                    
        return active_quests

    
    def find_completed_quests(self):
        data = self.read_file_content("quests.json")
        quests = []
        for quest_data in data['quests']:
                if quest_data['is_completed'] == True:
                    quests.append(DataMapper.map_dict_to_quest(quest_data))

        return quests
    

    def update_quest_status(self, quest_name, new_status):
      
        data = self.read_file_content("quests.json")

        for quest in data['quests']:
            if quest['name'] == quest_name:
                quest['is_completed'] = new_status
                break

        self.json_file_processor.write_to_file(self.get_path("quests.json"), data)
    


    def find_taverns_by_city(self, city):
        data = self.read_file_content("taverns.json")
        taverns: List[Tavern] = []

        for tavern_data in data['taverns']:
            if tavern_data['city'] == city:
                taverns.append(DataMapper.map_structures_to_class_object(tavern_data))

        return taverns
    
    def find_inns_by_city(self, city):
        data = self.read_file_content("inns.json")
        inns = []

        for inn_data in data['inns']:
            if inn_data['city'] == city:
                inns.append(DataMapper.map_structures_to_class_object(inn_data))

        return inns
    
    def find_shops_by_city(self, city):
        data = self.read_file_content("shops.json")
        return [DataMapper.map_structures_to_class_object(shop) for shop in data['shops']]
    
    def find_cities(self):
        data = self.read_file_content("cities.json")
        cities = []

        for city_data in data['cities']:
            cities.append(DataMapper.map_city_to_class_object(city_data))

        return cities
    
    def find_city_by_name(self, city_name):
        data = self.read_file_content("cities.json")
        cities = []

        for city_data in data['cities']:
            if city_data['name'] == city_name:
                cities.append(DataMapper.map_city_to_class_object(city_data))

        return cities

    def save_game(self, player):
        data = self.find_save_by_key("saves")
        

        if len(data) >= 3:
            data.sort(key=lambda x: x['last_save'])
            data.pop(0)

        player_info = player.to_dict()

        data.append({
            'title': player.name,
            'last_save': datetime.datetime.now().isoformat(),
            'player_info': player_info
        })

        self.json_file_processor.write_to_file(self.get_path("saves.json"), {'saves': data})

        return True

    def find_saves(self):
        data = self.read_file_content("saves.json")
        if data is None:
            raise ValueError("No data could be read from the file.")
        value = data["saves"]
        return value
        
    def find_items_by_rarity(self, rarity):
        data = self.read_file_content("items.json")
        items_of_rarity = [item for item in data['items'] if item['rarity'] == rarity]
        return [DataMapper.map_dict_to_item(item) for item in items_of_rarity]
    

    def find_open_fields_by_city(self, city):
        data = self.read_file_content("open_fields.json")

        for field_data in data['open_fields']:
            if field_data['city'] == city:
             return [DataMapper.map_structures_to_class_object(field_data)]
            
        return []
    

    def find_monsters(self):
        data = self.read_file_content("monsters.json")
        return [DataMapper.map_dict_to_monster(monster) for monster in data['monsters']]
    