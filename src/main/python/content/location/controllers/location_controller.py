from constants.constants import STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from content.inn.controllers.inn_controller import InnController
from content.location.models.location_model import LocationModel
from content.shop.controllers.shop_controller import ShopController
from content.tavern.controllers.tavern_controller import TavernController
from content.dungeon.controllers.dungeon_controller import DungeonController
from content.cave.controllers.cave_controller import CaveController
from content.open_fields.controllers.open_fields_controller import OpenFieldsController


class LocationController:
    def __init__(self, structure):
        self.location_model = LocationModel(structure)
        if structure.type == STRUCTURE_TYPE_DUNGEON:
            self.controller = DungeonController(structure)
        elif structure.type == STRUCTURE_TYPE_CAVE:
            self.controller = CaveController(structure)
        elif structure.type == STRUCTURE_TYPE_OPEN_FIELD:
            self.controller = OpenFieldsController(structure)
        elif structure.type == STRUCTURE_TYPE_SHOP:
            self.controller = ShopController(structure)
        elif structure.type == STRUCTURE_TYPE_TAVERN:
            self.controller = TavernController(structure)
        elif structure.type == STRUCTURE_TYPE_INN:
            self.controller = InnController(structure)