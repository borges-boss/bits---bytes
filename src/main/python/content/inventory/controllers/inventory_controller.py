from content.inventory.models.inventory_model import InventoryModel

class InventoryController:
    def __init__(self):
        self.model = InventoryModel()

    def get_items(self):
        return self.model.get_items()