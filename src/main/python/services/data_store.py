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
        data = self.json_file_processor.read_file_contents("datastore\data.json")
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
    

    def save_game(self, player, title):
        data = self.find_data_by_key('saves')

        if len(data) >= 4:
            data.sort(key=lambda x: x['last_save'])
            data.pop(0)

        player_info = {
            'player_id': player._player_id,
            'mana': player._mana,
            'game_class': player._game_class,
            'abilities': [vars(ability) for ability in player._abilities],
            'level': player._level,
            'xp': player._xp,
            'wallet': vars(player._wallet),
            'inventory': {**vars(player._inventory), 'items': [vars(item) for item in player._inventory._items]},
            'equipped_item': vars(player._equipped_item),
            'equipped_armor': [vars(item) for item in player._equiped_armor],
            'journal': {**vars(player._journal), 'quests': [vars(quest) for quest in player._journal._quests]},
            'name': player.name,
            'health': player.health,
            'race': player.race,
            'city': vars(player.city) 
        }

        data.append({
            'title': title,
            'last_save': datetime.now().isoformat(),
            'player_info': player_info
        })

        self.json_file_processor.write_to_file("datastore\\saves.json", {'saves': data})