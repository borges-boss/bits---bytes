import datetime
from base.journal import Journal
from base.wallet import Wallet
from classes.cave import Cave
from classes.damage_item import DamageItem
from classes.dungeon import Dungeon
from classes.inn import Inn
from classes.inventory import Inventory
from classes.open_fields import OpenFields
from classes.player import Player
from classes.shop import Shop
from classes.tavern import Tavern
from classes.wearable_item import WearableItem
from constants.constants import ITEM_TYPE_CONSUMABLE, ITEM_TYPE_DAMAGE, ITEM_TYPE_WEARABLE, STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from base.ability import Ability
from classes.consumable_item import ConsumableItem
from base.quest import Quest
from services.data_store import DataStore


class GameSaveModel:

    def __init__(self):
        self.datastore = DataStore()

    def parse_player_info(self, player_info) -> Player:
        wallet = Wallet(player_info['wallet']['coins'])
        inventory_items = []
        for item_data in player_info['inventory']['items']:
            if item_data['type'] == ITEM_TYPE_DAMAGE:
                item = DamageItem(item_data['name'], item_data['type'], item_data['rarity'], item_data['weight'],
                                 item_data['enchantments'], item_data['damage'])
            elif item_data['type'] == ITEM_TYPE_CONSUMABLE:
                item = ConsumableItem(item_data['name'], item_data['type'], item_data['rarity'], item_data['weight'],
                                     item_data['consumable_type'], item_data['effect_value'], item_data['effect_type'])
            elif item_data['type'] == ITEM_TYPE_WEARABLE:
                item = WearableItem(item_data['name'], item_data['type'], item_data['rarity'], item_data['weight'],
                                   item_data['enchantments'], item_data['defence'], item_data['wearable_type'])
            else:
                raise ValueError(f"Unknown item type: {item_data['type']}")
            
            inventory_items.append(item)

        inventory = Inventory(inventory_items, player_info['inventory']['max_weight'])
        equipped_item = DamageItem(player_info['equipped_item']['name'], player_info['equipped_item']['type'],
                                   player_info['equipped_item']['rarity'], player_info['equipped_item']['weight'],
                                   player_info['equipped_item']['enchantments'], player_info['equipped_item']['damage'])
        equipped_armor = [WearableItem(item['name'], item['type'], item['rarity'], item['weight'], item['enchantments'], item['defense']) 
                          for item in player_info['equipped_armor']]
        
        quests = []
        for quest_data in player_info['journal']['quests']:
            reward = quest_data['reward']
            if quest_data['reward_type'] == 'item':
                if reward['type'] == ITEM_TYPE_DAMAGE:
                    reward = DamageItem(reward['name'], reward['type'], reward['rarity'], reward['weight'],
                                        reward['enchantments'], reward['damage'])
                elif reward['type'] == ITEM_TYPE_CONSUMABLE:
                    reward = ConsumableItem(reward['name'], reward['type'], reward['rarity'], reward['weight'],
                                            reward['consumable_type'], reward['effect_value'], reward['effect_type'])
                elif reward['type'] == ITEM_TYPE_WEARABLE:
                    reward = WearableItem(reward['name'], reward['type'], reward['rarity'], reward['weight'],
                                        reward['enchantments'], reward['defence'], reward['wearable_type'])
                else:
                    raise ValueError(f"Unknown item type: {reward['type']}")

            quest = Quest(quest_data['name'], quest_data['description'], reward, quest_data['reward_type'], quest_data['is_completed'])
            quests.append(quest)

        journal = Journal(quests)
        
        location_type = player_info['location']['type']
        location = None
        
        if location_type == STRUCTURE_TYPE_DUNGEON:
            location = Dungeon(player_info['location']['name'], location_type, player_info['location']['dificulty'],
                               player_info['location']['chests_opened'], player_info['location']['layers'],
                               player_info['location']['bosses'], player_info['location']['chest_count'],
                               player_info['location']['monsters'])
        elif location_type == STRUCTURE_TYPE_CAVE:
            location = Cave(player_info['location']['name'], location_type, player_info['location']['dificulty'],
                            player_info['location']['monsters'], player_info['location']['ores'])
        elif location_type == STRUCTURE_TYPE_OPEN_FIELD:
            location = OpenFields(player_info['location']['name'], location_type, player_info['location']['width'],
                                  player_info['location']['height'], player_info['location']['dificulty']
                                  ,player_info['location']['monsters'],player_info['location']['structures'],player_info['city'])
        elif location_type == STRUCTURE_TYPE_SHOP:
            location = Shop(player_info['location']['name'], location_type, player_info['location']['width'],
                            player_info['location']['height'], player_info['location']['shopkeeper'],
                            player_info['location']['type_of_goods'], player_info['location']['items_for_sale'],player_info['city'])
        elif location_type == STRUCTURE_TYPE_TAVERN:
            location = Tavern(player_info['location']['name'], location_type, player_info['location']['width'],
                              player_info['location']['height'], player_info['location']['tavern_keeper'],
                              player_info['location']['quests'], player_info['location']['tavern_keeper_dialog'],player_info['city'])
        elif location_type == STRUCTURE_TYPE_INN:
            location = Inn(player_info['location']['name'], location_type, player_info['location']['width'],
                           player_info['location']['height'], player_info['location']['inkeeper'],
                           player_info['location']['rooms'], player_info['location']['price_per_stay'],player_info['city'])
            
        abilities = [Ability(ability['name'], ability['description'], ability['type'], ability['value'], ability['ability_cost']) 
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