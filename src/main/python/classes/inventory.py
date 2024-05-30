from python.base.item import Item
from typing import List

class Inventory:

    def __init__(self,items:List[Item],max_weight):
        self._items = items
        self.max_weight = max_weight


    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    def add_item(self, item:Item):
        total_weight = sum([i.weight for i in self.items])
        if item.weight + total_weight <= self.max_weight:
            self.items.append(item)
        else:
            print("You can't carry any more items.")

    def remove_item(self,item:Item):
        self.items.remove(item)



    