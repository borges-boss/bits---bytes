from content.shop.controllers.shop_controller import ShopController


class ShopView:
    def __init__(self, shop):
        self.controller = ShopController(shop)

    def display_items_for_sale(self):
        items = self.controller.get_items_for_sale()
        for item in items:
            print(f"Item: {item.name}, Type: {item.type}, Price: {item.price}")

    def handle_input(self, input):
        if input == "1":
            # Implement logic to choose an item to buy and call self.controller.buy_item(item)
            pass
        elif input == "2":
            # Implement logic to choose an item to sell and call self.controller.sell_item(item)
            pass
        elif input == "3":
            # Call methods to open inventory or journal
            pass
        elif input == "4":
            # Implement logic to leave the shop
            pass
        else:
            print("Invalid option.")