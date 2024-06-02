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
from constants.constants import STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from services.data_store import DataStore


class GameSaveModel:

    def __init__(self):
        self.datastore = DataStore()

    def parse_player_info(self, player_info) -> Player:
        wallet = Wallet(player_info['wallet']['_coins'])
        inventory = Inventory(player_info['inventory']['_items'], player_info['inventory']['max_weight'])
        equipped_item = DamageItem(player_info['equipped_item']['_name'], player_info['equipped_item']['_type'],
                                   player_info['equipped_item']['_rarity'], player_info['equipped_item']['_weight'],
                                   player_info['equipped_item']['_enchantments'], player_info['equipped_item']['_damage'])
        equipped_armor = [WearableItem(item['_name'], item['_type'], item['_rarity'], item['_weight'], item['_enchantments'], item['_defense']) 
                          for item in player_info['equipped_armor']]
        journal = Journal(player_info['journal']['_quests'])
        
        location_type = player_info['location']['_type']
        location = None
        
        if location_type == STRUCTURE_TYPE_DUNGEON:
            location = Dungeon(player_info['location']['_name'], location_type, player_info['location']['_dificulty'],
                               player_info['location']['_chests_opened'], player_info['location']['_layers'],
                               player_info['location']['_bosses'], player_info['location']['_chest_count'],
                               player_info['location']['_monsters'])
        elif location_type == STRUCTURE_TYPE_CAVE:
            location = Cave(player_info['location']['_name'], location_type, player_info['location']['_dificulty'],
                            player_info['location']['_monsters'], player_info['location']['_ores'])
        elif location_type == STRUCTURE_TYPE_OPEN_FIELD:
            location = OpenFields(player_info['location']['_name'], location_type, player_info['location']['_width'],
                                  player_info['location']['_height'], player_info['location']['_dificulty'],
                                  player_info['location']['_loot'], player_info['location']['_monsters'])
        elif location_type == STRUCTURE_TYPE_SHOP:
            location = Shop(player_info['location']['_name'], location_type, player_info['location']['_width'],
                            player_info['location']['_height'], player_info['location']['_shopkeeper'],
                            player_info['location']['_type_of_goods'], player_info['location']['_items_for_sale'])
        elif location_type == STRUCTURE_TYPE_TAVERN:
            location = Tavern(player_info['location']['_name'], location_type, player_info['location']['_width'],
                              player_info['location']['_height'], player_info['location']['_tavern_keeper'],
                              player_info['location']['_quests'], player_info['location']['_tavern_keeper_dialog'])
        elif location_type == STRUCTURE_TYPE_INN:
            location = Inn(player_info['location']['_name'], location_type, player_info['location']['_width'],
                           player_info['location']['_height'], player_info['location']['_inkeeper'],
                           player_info['location']['_rooms'], player_info['location']['_price_per_stay'])
            

        player = Player(player_info['health'], player_info['mana'], player_info['player_id'], player_info['name'], player_info['race'],
                        player_info['game_class'], player_info['abilities'], player_info['level'], player_info['xp'], wallet, inventory,
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
        saved = self.datastore.save_game(player)
        if saved:
            print("Seu jogo foi salvo com sucesso!")