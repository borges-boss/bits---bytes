from classes.pacific_structure import PacificStructure
from classes.npc import Npc
from base.item import Item
from typing import List

class Shop(PacificStructure):

    def __init__(self, name, type, width, height, shopkeeper:Npc, type_of_goods: List[Item], items_for_sale: List[Item]):
        super().__init__(name, type, width, height, [])
        self._shopkeeper = shopkeeper
        self._type_of_goods = type_of_goods
        self._items_for_sale = items_for_sale

    @property
    def shopkeeper(self):
        return self._shopkeeper

    @shopkeeper.setter
    def shopkeeper(self, value):
        self._shopkeeper = value

    @property
    def type_of_goods(self):
        return self._type_of_goods

    @type_of_goods.setter
    def type_of_goods(self, value):
        self._type_of_goods = value

    @property
    def items_for_sale(self):
        return self._items_for_sale

    @items_for_sale.setter
    def items_for_sale(self, value):
        self._items_for_sale = value


    def get_type_of_goods_for_sale(self):
        pass

    def is_shop_open(self):
        return True


        