from classes.npc import Npc
from classes.pacific_structure import PacificStructure
from classes.player import Player
from utils.print_utils import PrintUtils

class Inn(PacificStructure):

    def __init__(self, name, type, width, height, inkeeper: Npc, rooms, price_per_stay):
        super().__init__(name, type, width, height, [])
        self._inkeeper = inkeeper
        self._rooms = rooms
        self._price_per_stay = price_per_stay

    @property
    def inkeeper(self):
        return self._inkeeper

    @inkeeper.setter
    def inkeeper(self, value):
        self._inkeeper = value

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    @property
    def price_per_stay(self):
        return self._price_per_stay

    @price_per_stay.setter
    def price_per_stay(self, value):
        self._price_per_stay = value

    def rest(self, player:Player):
        if player.wallet.coins >= self.price_per_stay:
            player.wallet.subtract_coins(self.price_per_stay)
            player.helth(player.calculate_max_health()) #Restaurar vida completa do jogador
            return player
        else:
            PrintUtils.print_entity_dialog(self.inkeeper,"Só volte aqui quando tiver grana pra pagar pelo quarto!")
            print("Voce nao tem moedas o suficiente para pagar por um quarto")
            return player

    def print_inn_details(self):
        print(f"Inn Name: {self.name}")
        print(f"Inkeeper: {self.inkeeper.name}")
        print(f"Price per Stay: {self.price_per_stay}")

