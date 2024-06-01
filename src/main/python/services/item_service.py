from classes.consumable_item import ConsumableItem
from classes.damage_item import DamageItem
from classes.wearable_item import WearableItem
from constants.constants import ITEM_TYPE_CONSUMABLE, ITEM_TYPE_DAMAGE, ITEM_TYPE_WEARABLE


class ItemService:
    
    @staticmethod
    def map_to_item(item_json):
        if item_json['_type'] == ITEM_TYPE_DAMAGE:
            return DamageItem(item_json['_name'], item_json['_type'], item_json['_rarity'], item_json['_weight'],
                            item_json['_enchantments'], item_json['_damage'])
        elif item_json['_type'] == ITEM_TYPE_WEARABLE:
            return WearableItem(item_json['_name'], item_json['_type'], item_json['_rarity'], item_json['_weight'],
                                item_json['_enchantments'], item_json['_defence'], item_json['_wearable_type'])
        elif item_json['_type'] == ITEM_TYPE_CONSUMABLE:
            return ConsumableItem(item_json['_name'], item_json['_type'], item_json['_rarity'], item_json['_weight'],
                                item_json['_consumable_type'], item_json['_effect_value'], item_json['_effect_type'])
        else:
            raise ValueError(f"Invalid item type: {item_json['_type']}")