from content.shop.models.shop_model import ShopModel

class ShopController:
    def __init__(self, shop):
        self.model = ShopModel(shop)

    def get_items_for_sale(self):
        return self.model.get_items_for_sale()

    def buy_item(self, item):
        self.model.buy_item(item)

    def sell_item(self, item):
        self.model.sell_item(item)