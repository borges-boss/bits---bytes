import datetime
from base.item import Item
from base.quest import Quest
from classes.npc import Npc
from classes.tavern import Tavern
from typing import List
from services.json_file_proc import JsonFileProcessor

class DataStore:
    def __init__(self):
      self.json_file_processor = JsonFileProcessor()


    def find_data_by_key(self, key):
        data = self.json_file_processor.read_file_contents("datastore\\saves.json")
        if data and key in data:
            value = data[key]
            return value if isinstance(value, list) else [value]
        else:
            return []
        
    
    def find_quests_by_city(self, city):
        data = self.json_file_processor.read_file_contents("datastore\quests.json")
        quests = []
        for quest_data in data['quests']:
            if quest_data['city'] == city:
                reward_type = quest_data['reward']['type']
                reward = quest_data['reward']['value']
                if reward_type == 'item':
                    reward = Item(**reward)
                quest = Quest(quest_data['name'], quest_data['description'], reward, reward_type, quest_data['is_completed'])
                quests.append(quest)

        return quests
    


    def find_active_quests(self):
        data = self.json_file_processor.read_file_contents("datastore\quests.json")
        quests = []
        for quest_data in data['quests']:
                if quest_data['is_completed'] == False:
                    reward_type = quest_data['reward']['type']
                    reward = quest_data['reward']['value']
                    if reward_type == 'item':
                        reward = Item(**reward)
                    quest = Quest(quest_data['name'], quest_data['description'], reward, reward_type, quest_data['is_completed'])
                    quests.append(quest)

        return quests
    
    def find_completed_quests(self):
        data = self.json_file_processor.read_file_contents("datastore\quests.json")
        quests = []
        for quest_data in data['quests']:
                if quest_data['is_completed'] == True:
                    reward_type = quest_data['reward']['type']
                    reward = quest_data['reward']['value']
                    if reward_type == 'item':
                        reward = Item(**reward)
                    quest = Quest(quest_data['name'], quest_data['description'], reward, reward_type, quest_data['is_completed'])
                    quests.append(quest)

        return quests
    

    def update_quest_status(self, quest_name, new_status):
      
        data = self.json_file_processor.read_file_contents("datastore\\quests.json")

        for quest in data['quests']:
            if quest['name'] == quest_name:
                quest['is_completed'] = new_status
                break

        self.json_file_processor.write_to_file("datastore\\quests.json", data)
    


    def find_taverns_by_city(self, city):
        data = self.json_file_processor.read_file_contents("datastore\\taverns.json")
        taverns: List[Tavern] = []

        for tavern_data in data['taverns']:
            if tavern_data['city'] == city:
                tavern_keeper_data = tavern_data['tavern_keeper']
                tavern_keeper = Npc(tavern_keeper_data['health'], tavern_keeper_data['defence'],
                                    tavern_keeper_data['race'], tavern_keeper_data['type'],
                                    tavern_keeper_data['name'], tavern_keeper_data['description'],
                                    tavern_keeper_data['role'])
                quests = []
                for quest_data in tavern_data['quests']:
                    reward_type = quest_data['reward']['type']
                    reward = quest_data['reward']['value']
                    if reward_type == 'item':
                        reward = Item(**reward)
                    quest = Quest(quest_data['name'], quest_data['description'], reward, reward_type, quest_data['is_completed'])
                    quests.append(quest)
                tavern = Tavern(tavern_data['name'], tavern_data['type'], tavern_data['width'],
                                tavern_data['height'], tavern_keeper, quests, tavern_data['tavern_keeper_dialog'])
                taverns.append(tavern)

        return taverns
    

    def save_game(self, player):
        data = self.find_data_by_key('saves')
        

        if len(data) >= 4:
            data.sort(key=lambda x: x['last_save'])
            data.pop(0)

        player_info = {
            'player_id': player.player_id,
            'mana': player.mana,
            'game_class': player.game_class,
            'abilities': [vars(ability) for ability in player.abilities],
            'level': player.level,
            'xp': player.xp,
            'wallet': vars(player.wallet),
            'inventory': {**vars(player.inventory), 'items': [vars(item) for item in player.inventory.items]},
            'equipped_item': vars(player.equipped_item),
            'equipped_armor': [vars(item) for item in player.equiped_armor],
            'journal': {**vars(player.journal), 'quests': [vars(quest) for quest in player.journal.quests]},
            'name': player.name,
            'health': player.health,
            'race': player.race,
            'location': vars(player.location) 
        }

        data.append({
            'title': "Save "+str((len(data) + 1)),
            'last_save': datetime.datetime.now().isoformat(),
            'player_info': player_info
        })

        self.json_file_processor.write_to_file("datastore\\saves.json", {'saves': data})

        return True

    def find_saves(self):
        data = self.json_file_processor.read_file_contents("datastore\\saves.json")
        value = data["saves"]
        return value
    
    def find_items_by_rarity(self, rarity):
        data = self.json_file_processor.read_file_contents("datastore\\items.json")
        items_of_rarity = [item for item in data['items'] if item['_rarity'] == rarity]
        return items_of_rarity

    def find_locations_by_city(self):
        pass