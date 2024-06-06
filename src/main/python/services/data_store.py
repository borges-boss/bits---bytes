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
from base.ability import Ability
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
                reward_type = quest_data['reward_type']
                reward = quest_data['reward']
                if reward_type == 'item':
                        item_type = reward['type']
                        if item_type == ITEM_TYPE_DAMAGE:
                            reward = DamageItem(**reward)
                        elif item_type == ITEM_TYPE_CONSUMABLE:
                            reward = ConsumableItem(**reward)
                        elif item_type == ITEM_TYPE_WEARABLE:
                            reward = WearableItem(**reward)
                            
                quest = Quest(quest_data['name'], quest_data['description'], reward, reward_type, quest_data['is_completed'])
                quests.append(quest)

        return quests
    


    def find_active_quests(self):
        data = self.read_file_content("saves.json")
        active_quests = []
        for save in data['saves']:
            for quest in save['player_info']['journal']['quests']:
                if not quest['is_completed']:
                    reward_type = quest['reward_type']
                    reward = quest['reward']

                    if reward_type == 'item':
                        item_type = reward['type']
                        if item_type == ITEM_TYPE_DAMAGE:
                            reward = DamageItem(**reward)
                        elif item_type == ITEM_TYPE_CONSUMABLE:
                            reward = ConsumableItem(**reward)
                        elif item_type == ITEM_TYPE_WEARABLE:
                            reward = WearableItem(**reward)

                active_quests.append(Quest(quest['name'], quest['description'], reward, reward_type, quest['is_completed']))
                    
        return active_quests

    
    def find_completed_quests(self):
        data = self.read_file_content("quests.json")
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
                tavern_keeper_data = tavern_data['tavern_keeper']
                tavern_keeper = Npc(tavern_keeper_data['health'], tavern_keeper_data['defence'],
                                    tavern_keeper_data['race'], tavern_keeper_data['type'],
                                    tavern_keeper_data['name'], tavern_keeper_data['description'],
                                    tavern_keeper_data['role'])
                quests = []
                for quest_data in tavern_data['quests']:
                    reward_type = quest_data['reward_type']
                    reward = quest_data['reward']
                    if reward_type == 'item':
                        item_type = reward['type']
                        if item_type == ITEM_TYPE_DAMAGE:
                            reward = DamageItem(**reward)
                        elif item_type == ITEM_TYPE_CONSUMABLE:
                            reward = ConsumableItem(**reward)
                        elif item_type == ITEM_TYPE_WEARABLE:
                            reward = WearableItem(**reward)

                    quest = Quest(quest_data['name'], quest_data['description'], reward, reward_type, quest_data['is_completed'])
                    quests.append(quest)
                tavern = Tavern(tavern_data['name'], tavern_data['type'], tavern_data['width'],
                                tavern_data['height'], tavern_keeper, quests, tavern_data['tavern_keeper_dialog'],tavern_data['city'])
                taverns.append(tavern)

        return taverns
    
    def find_inns_by_city(self, city):
        data = self.read_file_content("inns.json")
        inns = []

        for inn_data in data['inns']:
            if inn_data['city'] == city:
                innkeeper_data = inn_data['innkeeper']
                innkeeper = Npc(innkeeper_data['health'], innkeeper_data['defence'],
                                innkeeper_data['race'], innkeeper_data['type'],
                                innkeeper_data['name'], innkeeper_data['description'],
                                innkeeper_data['role'])
                rooms = inn_data['rooms']
                price_per_stay = inn_data['price_per_stay']
                inn = Inn(inn_data['name'], inn_data['type'], inn_data['width'],
                        inn_data['height'], innkeeper, rooms, price_per_stay,inn_data['city'])
                inns.append(inn)

        return inns
    
    def find_shops_by_city(self, city):
        data = self.read_file_content("shops.json")
        shops = []

        for shop_data in data['shops']:
            if shop_data['city'] == city:
                shopkeeper_data = shop_data['shopkeeper']
                shopkeeper = Npc(shopkeeper_data['health'], shopkeeper_data['defence'],
                                shopkeeper_data['race'], shopkeeper_data['type'],
                                shopkeeper_data['name'], shopkeeper_data['description'],
                                shopkeeper_data['role'])
                items = []
                for item_data in shop_data['items_for_sale']:
                    enchantments = [Enchantment(**enchantment_data) for enchantment_data in item_data.get('enchantments', [])]
                    if item_data['type'] == ITEM_TYPE_DAMAGE:
                        item = DamageItem(item_data['name'], item_data['type'], item_data['rarity'], 
                                        item_data['weight'], enchantments, item_data['damage'])
                    elif item_data['type'] == ITEM_TYPE_WEARABLE:
                        item = WearableItem(item_data['name'], item_data['type'], item_data['rarity'], 
                                            item_data['weight'], enchantments, item_data['defence'], 
                                            item_data['wearable_type'])
                    elif item_data['type'] == ITEM_TYPE_CONSUMABLE:
                        item = ConsumableItem(item_data['name'], item_data['type'], item_data['rarity'], 
                                            item_data['weight'], item_data['consumable_type'], 
                                            item_data['effect_value'], item_data['effect_type'])
                    else:
                        print(f"Tipo de item desconhecido: {item_data['type']}")
                        continue
                    items.append(item)

                shop = Shop(shop_data['name'], shop_data['type'], shop_data['width'],
                            shop_data['height'], shopkeeper, items, shop_data['city'])
                shops.append(shop)

        return shops
    
    def find_cities(self):
        data = self.read_file_content("cities.json")
        cities = []

        for city_data in data['cities']:
            structures = []
            for structure_data in city_data.get('structures', []):
                if structure_data['type'] == STRUCTURE_TYPE_INN:
                    structure = Inn(**structure_data)
                elif structure_data['type'] == STRUCTURE_TYPE_TAVERN:
                    structure = Tavern(**structure_data)
                elif structure_data['type'] == STRUCTURE_TYPE_OPEN_FIELD:
                    structure = OpenFields(**structure_data)
                elif structure_data['type'] == STRUCTURE_TYPE_SHOP:
                    structure = Shop(**structure_data)
                else:
                    print(f"Unknown structure type: {structure_data['type']}")
                    continue
                structures.append(structure)
            city = City(city_data['width'], city_data['height'], city_data['name'], 
                        city_data['description'], structures)
            cities.append(city)

        return cities
    
    def find_city_by_name(self, city_name):
        data = self.read_file_content("cities.json")

        for city_data in data['cities']:
            if city_data['name'] == city_name:
                structures = []
                for structure_data in city_data.get('structures', []):
                    if structure_data['type'] == STRUCTURE_TYPE_INN:
                        innkeeper = Npc(**structure_data['inkeeper'])
                        structure_data['inkeeper'] = innkeeper
                        structure = Inn(**structure_data)
                    elif structure_data['type'] == STRUCTURE_TYPE_TAVERN:
                        tavern_keeper = Npc(**structure_data['tavern_keeper'])
                        quests = [Quest(**q) for q in structure_data['quests']]
                        structure_data['tavern_keeper'] = tavern_keeper
                        structure_data['quests'] = quests
                        structure = Tavern(**structure_data)
                    elif structure_data['type'] == STRUCTURE_TYPE_OPEN_FIELD:
                        monsters = []
                        for monster_data in structure_data['monsters']:
                            abilities = [Ability(**a) for a in monster_data['abilities']]
                            monster_data['abilities'] = abilities
                            monster = Monster(**monster_data)
                            monsters.append(monster)
                        structure_data['monsters'] = monsters
                        structure = OpenFields(**structure_data)
                    elif structure_data['type'] == STRUCTURE_TYPE_SHOP:
                        shopkeeper = Npc(**structure_data['shopkeeper'])
                        items_for_sale = []
                        for item_data in structure_data['items_for_sale']:
                            item_type = item_data['type']
                            if item_type == ITEM_TYPE_DAMAGE:
                                item = DamageItem(**item_data)
                            elif item_type == ITEM_TYPE_CONSUMABLE:
                                item = ConsumableItem(**item_data)
                            elif item_type == ITEM_TYPE_WEARABLE:
                                item = WearableItem(**item_data)
                            items_for_sale.append(item)
                        structure_data['shopkeeper'] = shopkeeper
                        structure_data['items_for_sale'] = items_for_sale
                        structure = Shop(**structure_data)
                    else:
                        print(f"Unknown structure type: {structure_data['type']}")
                        continue
                    structures.append(structure)
                return City(city_data['width'], city_data['height'], city_data['name'], 
                            city_data['description'], structures)

        return None

    def save_game(self, player):
        data = self.find_save_by_key("saves")
        

        if len(data) >= 4:
            data.sort(key=lambda x: x['last_save'])
            data.pop(0)

        player_info = player.to_dict()

        data.append({
            'title': "Save "+str((len(data) + 1)),
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
        return items_of_rarity
    

    def find_open_fields_by_city(self, city):
        data = self.read_file_content("open_fields.json")
        open_fields = []

        for field_data in data['open_fields']:
            if field_data['city'] == city:
                monsters = []
                for monster_data in field_data['monsters']:
                    monster = Monster(monster_data['health'], monster_data['damage'], monster_data['defence'],
                                    monster_data['stamina'], monster_data['race'], monster_data['type'],
                                    monster_data['name'], monster_data['mana'], monster_data['description'],
                                    monster_data['abilities'], monster_data['level'])
                    monsters.append(monster)

                structures = []
                for structure_data in field_data['structures']:
                    if structure_data['type'] == STRUCTURE_TYPE_DUNGEON:
                        structure = Dungeon(structure_data['name'], structure_data['type'], structure_data['dificulty'],
                                            structure_data['chests_opened'], structure_data['layers'], 
                                            structure_data['bosses'], structure_data['chest_count'], 
                                            structure_data['monsters'])
                    elif structure_data['type'] == STRUCTURE_TYPE_CAVE:
                        structure = Cave(structure_data['name'], structure_data['type'], structure_data['dificulty'],
                                        structure_data['monsters'], structure_data['ores'])
                    else:
                        print(f"Unknown structure type: {structure_data['type']}")
                        continue
                    structures.append(structure)

                open_field = OpenFields(field_data['name'], field_data['type'], field_data['width'],
                            field_data['height'], field_data['dificulty'], monsters, structures, field_data['city'])
                open_fields.append(open_field)

        return open_fields
    

    def find_monsters(self):
        data = self.read_file_content("monsters.json")
        monsters_data = data['monsters']

        monsters = []
        for monster_data in monsters_data:
            monster = Monster(
                health=monster_data['health'],
                damage=monster_data['damage'],
                defence=monster_data['defence'],
                stamina=monster_data['stamina'],
                race=monster_data['race'],
                type=monster_data['type'],
                name=monster_data['name'],
                mana=monster_data['mana'],
                description=monster_data['description'],
                abilities=monster_data['abilities'],
                level=monster_data['level']
            )
            monsters.append(monster)

        return monsters
    