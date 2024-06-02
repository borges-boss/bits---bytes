class Wallet:

    def __init__(self,coins:float):
        self._coins = coins

    @property
    def coins(self):
        return self._coins

    def add_coins(self, value:float):
        self._coins += value

    def subtract_coins(self, value:float):
        if self._coins >= value:
            self._coins -= value
        else:
            print("Voce nao tem coins suficientes")
