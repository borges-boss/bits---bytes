import random
from constants.constants import ITEM_RARITY_COMMON, ITEM_RARITY_EPIC, ITEM_RARITY_LEGENDARY, ITEM_RARITY_RARE
from services.data_store import DataStore


class LootService:

    def __init__(self):
        pass

    @staticmethod
    def get_random_loot_from_monster(monster):
        datastore = DataStore()
        items = []
        if monster.level <= 5:
            items = datastore.find_items_by_rarity(rarity=ITEM_RARITY_COMMON)
        elif monster.level <= 10:
            items = datastore.find_items_by_rarity(rarity=ITEM_RARITY_RARE)
        elif monster.level <= 15:
            items = datastore.find_items_by_rarity(rarity=ITEM_RARITY_EPIC)
        else:
            items = datastore.find_items_by_rarity(rarity=ITEM_RARITY_LEGENDARY)

        if random.random() < 0.25:
            return None

        return random.choice(items) if items else None
