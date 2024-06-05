class Inventory:

    def __init__(self,items,max_weight):
        self._items = items
        self.max_weight = max_weight


    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    def add_item(self, item):
        total_weight = sum([i.weight for i in self.items])
        if item.weight + total_weight <= self.max_weight:
            print("\nVoce adicionou "+item.name+" ao seu inventario")
            self.items.append(item)
            return True
        else:
            print("Voce não consegue carregar mais itens.")
            return False
        

    def to_dict(self):
        return {
            'items': [item.to_dict() for item in self.items],
            'max_weight': self.max_weight
        }

    def remove_item(self,item):
        self.items.remove(item)
        return True



    