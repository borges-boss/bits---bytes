class InventoryView:

    @staticmethod
    def open_inventory(items):
        if not items:
            print("Your inventory is empty.")
        else:
            for item in items:
                print(f"Item: {item.name}, Type: {item.type}, Weight: {item.weight}")
