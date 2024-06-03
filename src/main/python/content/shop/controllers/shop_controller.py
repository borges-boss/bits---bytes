from content.shop.models.shop_model import ShopModel

class ShopController:
    def __init__(self):
        self.model = ShopModel()

    def get_items_for_sale(self):
        return self.model.get_items_for_sale()
    
    def evaluate_item_price(self, item):
        return self.model.evaluate_item_price(item)

    def buy_item(self, item):
        self.model.buy_item(item)

    def sell_item(self, item):
        self.model.sell_item(item)

    def open_inventory(self):
        self.model.open_inventory()

    def open_journal(self):
        self.model.open_journal()

    def leave(self):
        self.model.leave()