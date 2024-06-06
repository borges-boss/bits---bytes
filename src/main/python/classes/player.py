from base.entity import Entity
from base.wallet import Wallet
from classes.inventory import Inventory
from classes.wearable_item import WearableItem
from classes.damage_item import DamageItem
from base.journal import Journal
from typing import List

from base.ability import Ability



class Player(Entity):

    def __init__(self, health=100, mana=100, stamina=100, player_id=0, name="", race="", game_class="", abilities:List[Ability]=[], level=1, xp=0, wallet:Wallet=None, inventory:Inventory=None, 
                 equipped_item: DamageItem=None, equipped_armor:List[WearableItem]=[], journal: Journal=None, location=None, city=""):
        self._player_id = player_id
        self._mana = mana
        self._stamina = stamina
        self._game_class = game_class
        self._abilities = abilities
        self._level = level
        self._xp = xp
        self._wallet = wallet
        self._inventory = inventory
        self._equipped_item = equipped_item
        self._equiped_armor = equipped_armor
        self._journal = journal
        self._location = location # Dungeon, Cave, OpenFiedl, Shop, Tavern, Inn
        self._city = city
        super().__init__(name, health, 0, 0, stamina, race, None)



    def to_dict(self):
        return {
            'player_id': self._player_id,
            'mana': self._mana,
            'stamina': self._stamina,
            'game_class': self._game_class,
            'abilities': [ability.to_dict() for ability in self.abilities],
            'level': self._level,
            'xp': self._xp,
            'wallet': self._wallet.to_dict(),
            'inventory': self._inventory.to_dict(),
            'equipped_item': self._equipped_item.to_dict(),
            'equipped_armor': [item.to_dict() for item in self._equiped_armor],
            'journal': self._journal.to_dict(),
            'name': self.name,
            'health': self.health,
            'race': self.race,
            'location': self._location.to_dict() if self._location!= None else "",
            'city': self._city
        }


    def abilities_to_dict(self):
            return [{
            'name': ability.name,
            'type': ability.type,
            'description': ability.description,
            'value': ability.value,
            'ability_cost': ability.ability_cost
        } for ability in self.abilities]

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def equiped_armor(self):
        return self._equiped_armor
    
    @equiped_armor.setter
    def equiped_armor(self, value):
        self._equipped_armor = value

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
        
    @property
    def journal(self):
        return self._journal

    @journal.setter
    def journal(self, value):
        self._journal = value

    @property
    def equipped_armor(self):
        return self._equiped_armor

    @equipped_armor.setter
    def equipped_armor(self, value):
        self._equiped_armor = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        self._xp = value

    @property
    def equipped_item(self):
        return self._equipped_item

    @equipped_item.setter
    def equipped_item(self, value):
        self._equipped_item = value

    @property
    def inventory(self):
        return self._inventory

    @property
    def wallet(self):
        return self._wallet
    
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value

    @property
    def game_class(self):
        return self._game_class

    @game_class.setter
    def game_class(self, value):
        self._game_class = value

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, value):
        self._abilities = value





