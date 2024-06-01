from content.inventory.controllers.inventory_controller import InventoryController

class InventoryView:
    def __init__(self):
        self.controller = InventoryController()

    def display_items(self):
        items = self.controller.get_items()
        for item in items:
            print(f"Item: {item.name}, Type: {item.type}, Weight: {item.weight}")