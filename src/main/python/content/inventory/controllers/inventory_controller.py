from content.inventory.models.inventory_model import InventoryModel
from constants.constants import ITEM_TYPE_CONSUMABLE, ITEM_TYPE_DAMAGE, ITEM_TYPE_WEARABLE
from content.player.controllers.player_controller import PlayerController

class InventoryController:
    def __init__(self):
        self.model = InventoryModel()

    def get_player_items(self):
        return self.model.get_items()
    
    def use_item(self, item):
        if item.type == ITEM_TYPE_CONSUMABLE:
            print(f"\nVoce usou {item.name}.")
        else:
            print(f"{item.name} is not a consumable item.")

    def equip_item(self, item):
        if item.type in [ITEM_TYPE_WEARABLE, ITEM_TYPE_DAMAGE]:
            print(f"\nVoce equipou {item.name}.")
            if item.type == ITEM_TYPE_WEARABLE:
                PlayerController.get_player().equip_piece_of_armor(item)
            else: 
                PlayerController.get_player().equip_item(item)
        else:
            print(f"{item.name} is not an equippable item.")