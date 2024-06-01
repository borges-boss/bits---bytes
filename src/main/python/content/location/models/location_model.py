from constants.constants import STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from content.inn.models.inn_model import InnModel
from content.shop.models.shop_model import ShopModel
from content.tavern.models.tavern_model import TavernModel
from content.dungeon.models.dungeon_model import DungeonModel
from content.cave.models.cave_model import CaveModel
from content.open_fields.models.open_fields_model import OpenFieldsModel


class LocationModel:
    def __init__(self, structure):
        if structure.type == STRUCTURE_TYPE_DUNGEON:
            self.model = DungeonModel(structure)
        elif structure.type == STRUCTURE_TYPE_CAVE:
            self.model = CaveModel(structure)
        elif structure.type == STRUCTURE_TYPE_OPEN_FIELD:
            self.model = OpenFieldsModel(structure)
        elif structure.type == STRUCTURE_TYPE_SHOP:
            self.model = ShopModel(structure)
        elif structure.type == STRUCTURE_TYPE_TAVERN:
            self.model = TavernModel(structure)
        elif structure.type == STRUCTURE_TYPE_INN:
            self.model = InnModel(structure)