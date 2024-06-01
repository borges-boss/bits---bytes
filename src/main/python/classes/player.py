from base.entity import Entity
from base.wallet import Wallet
from classes.inventory import Inventory
from base.ability import Ability
from classes.monster import Monster
from base.item import Item
from classes.consumable_item import ConsumableItem
from classes.wearable_item import WearableItem
from classes.damage_item import DamageItem
from base.journal import Journal
from typing import List
from constants.constants import ABILITY_TYPE_PHYSICAL
from constants.constants import ABILITY_TYPE_MAGIC
from constants.constants import ABILITY_TYPE_STATS_HEALTH
from constants.constants import ABILITY_TYPE_STATS_STAMINA
from constants.constants import ABILITY_TYPE_STATS_DAMAGE
from constants.constants import ABILITY_TYPE_STATS_DEFENCE
from constants.constants import ABILITY_TYPE_STATS_TARG_HEALTH
from constants.constants import ABILITY_TYPE_STATS_TARG_STAMINA
from constants.constants import ABILITY_TYPE_STATS_TARG_DAMAGE
from constants.constants import ABILITY_TYPE_STATS_TARG_DEFENCE
from constants.constants import ITEM_TYPE_DAMAGE
from constants.constants import CONSUMABLE_EFFECT_TYPE_MANA
from constants.constants import CLASS_TYPE_WARRIOR
from constants.constants import CLASS_TYPE_ASSASIN
from constants.constants import CLASS_TYPE_MAGE
from constants.constants import CLASS_TYPE_BATTLE_MAGE
from constants.constants import CLASS_TYPE_BERSERKER
from constants.constants import RACE_TYPE_HUMAN
from constants.constants import RACE_TYPE_DWARF
from constants.constants import RACE_TYPE_HALF_ELF
from constants.constants import RACE_TYPE_LIZARDFOLK
from constants.constants import RACE_TYPE_ORC



class Player(Entity):

    def __init__(self, health, mana, player_id, name, race, game_class: str , abilities, level, xp, wallet:Wallet, inventory:Inventory, 
                 equipped_item: DamageItem, equipped_armor:List[WearableItem], journal: Journal, city):
        self._player_id = player_id
        self._mana = mana
        self._game_class = game_class
        self._abilities = abilities
        self._level = level
        self._xp = xp
        self._wallet = wallet
        self._inventory = inventory
        self._equipped_item = equipped_item
        self._equiped_armor = equipped_armor
        self._journal = journal
        self._city = city
        super().__init__(name, health, 0, 0, race, None)


    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
        
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
        return self.xp

    @xp.setter
    def xp(self, value):
        self.xp = value

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

    # Override
    @property
    def damage(self):
        return self.get_player_damage()
    
    @property
    def defence(self):
        return self.get_player_defence()



    # Abilities

    def deal_damage(self,ability:Ability, target:Monster):
        # Calcular dano baseado no nivel do player e o dano base da abilidade
        damage = ability.value + self.damage

         # Calcular redução de dano baseado na defesa do alvo
        damage_reduction = target.defence / 100.0 

        # Aplicar redução de dano
        net_damage = damage * (1 - damage_reduction)

        # Subtrair dano liquido da vida do alvo
        target.health -= net_damage
        print(f"{self.name} usou {ability.name}! {target.name} levou {net_damage} de dano!")


    def use_stats_ability(self, ability:Ability, target:Monster):
        if self.mana >= ability.ability_cost:
            if ability.type == ABILITY_TYPE_STATS_HEALTH:
                self.health += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_STAMINA:
                self.stamina += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_DAMAGE:
                self.damage += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_DEFENCE:
                self.defence += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_TARG_HEALTH:
                target.health -= ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_TARG_STAMINA:
                target.stamina -= ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_TARG_DAMAGE:
                target.damage -= ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_TARG_DEFENCE:
                target.defence -= ability.effect_value
            else:
                print("Invalid ability type.")
            
            self.mana -= ability.ability_cost
        else:
            print("Not enough mana to use this ability.")


    def useAbility(self, ability:Ability, target:Monster):
        if ability.type == ABILITY_TYPE_PHYSICAL:
            if self.stamina >= ability.ability_cost:
                self.deal_damage(ability,target)
                self.stamina -= ability.ability_cost
            else:
                print("Not enough stamina to use this ability.")
        elif ability.type == ABILITY_TYPE_MAGIC:
            if self.mana >= ability.ability_cost:
                self.deal_damage(ability,target)
                self.mana -= ability.ability_cost
            else:
                print("Not enough mana to use this ability.")
        else:
            self.use_stats_ability(ability,target)

        return target


    # Stats

    def get_base_health(self):
        base_health = 100

        if self.game_class == CLASS_TYPE_WARRIOR:
            base_health += 50
        elif self.game_class == CLASS_TYPE_ASSASIN:
            base_health += 20
        elif self.game_class == CLASS_TYPE_MAGE:
            base_health += 10
        elif self.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_health += 30
        elif self.game_class == CLASS_TYPE_BERSERKER:
            base_health += 60

        if self.race == RACE_TYPE_HUMAN:
            base_health += 10
        elif self.race == RACE_TYPE_DWARF:
            base_health += 20
        elif self.race == RACE_TYPE_HALF_ELF:
            base_health += 15
        elif self.race == RACE_TYPE_LIZARDFOLK:
            base_health += 20
        elif self.race == RACE_TYPE_ORC:
            base_health += 25

        return base_health
        
    def get_base_mana(self):
        base_mana = 100

        if self.game_class == CLASS_TYPE_WARRIOR:
            base_mana += 20
        elif self.game_class == CLASS_TYPE_ASSASIN:
            base_mana += 30
        elif self.game_class == CLASS_TYPE_MAGE:
            base_mana += 60
        elif self.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_mana += 50
        elif self.game_class == CLASS_TYPE_BERSERKER:
            base_mana += 40

        if self.race == RACE_TYPE_HUMAN:
            base_mana += 10
        elif self.race == RACE_TYPE_DWARF:
            base_mana += 20
        elif self.race == RACE_TYPE_HALF_ELF:
            base_mana += 15
        elif self.race == RACE_TYPE_LIZARDFOLK:
            base_mana += 20
        elif self.race == RACE_TYPE_ORC:
            base_mana += 25

        return base_mana

    def get_base_stamina(self):
        base_stamina = 100

        if self.game_class == CLASS_TYPE_WARRIOR:
            base_stamina += 60
        elif self.game_class == CLASS_TYPE_ASSASIN:
            base_stamina += 50
        elif self.game_class == CLASS_TYPE_MAGE:
            base_stamina += 20
        elif self.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_stamina += 40
        elif self.game_class == CLASS_TYPE_BERSERKER:
            base_stamina += 70

        if self.race == RACE_TYPE_HUMAN:
            base_stamina += 10
        elif self.race == RACE_TYPE_DWARF:
            base_stamina += 20
        elif self.race == RACE_TYPE_HALF_ELF:
            base_stamina += 15
        elif self.race == RACE_TYPE_LIZARDFOLK:
            base_stamina += 20
        elif self.race == RACE_TYPE_ORC:
            base_stamina += 25

        return base_stamina
        
    def get_base_damage(self):
        base_damage = 10

        if self.game_class == CLASS_TYPE_WARRIOR:
            base_damage += 20
        elif self.game_class == CLASS_TYPE_ASSASIN:
            base_damage += 30
        elif self.game_class == CLASS_TYPE_MAGE:
            base_damage += 10
        elif self.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_damage += 15
        elif self.game_class == CLASS_TYPE_BERSERKER:
            base_damage += 25

        if self.race == RACE_TYPE_HUMAN:
            base_damage += 5
        elif self.race == RACE_TYPE_DWARF:
            base_damage += 10
        elif self.race == RACE_TYPE_HALF_ELF:
            base_damage += 7
        elif self.race == RACE_TYPE_LIZARDFOLK:
            base_damage += 10
        elif self.race == RACE_TYPE_ORC:
            base_damage += 12

        return base_damage

    def get_base_defence(self):
        base_defence = 10

        if self.game_class == CLASS_TYPE_WARRIOR:
            base_defence += 30
        elif self.game_class == CLASS_TYPE_ASSASIN:
            base_defence += 20
        elif self.game_class == CLASS_TYPE_MAGE:
            base_defence += 10
        elif self.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_defence += 20
        elif self.game_class == CLASS_TYPE_BERSERKER:
            base_defence += 40

        if self.race == RACE_TYPE_HUMAN:
            base_defence += 5
        elif self.race == RACE_TYPE_DWARF:
            base_defence += 10
        elif self.race == RACE_TYPE_HALF_ELF:
            base_defence += 7
        elif self.race == RACE_TYPE_LIZARDFOLK:
            base_defence += 10
        elif self.race == RACE_TYPE_ORC:
            base_defence += 12

        return base_defence

 
    def get_player_base_health(self):
        base_health = self.get_base_health() 
        health_per_level = 10

        return base_health + (self.level * health_per_level)
    

    def get_player_mana(self):
        base_mana = self.get_base_mana() 
        mana_per_level = 10

        return base_mana + (self.level * mana_per_level)
    

    def get_player_base_stamina(self):
        base_stamina = self.get_base_stamina() 
        stamina_per_level = 10

        return base_stamina + (self.level * stamina_per_level)


    def get_player_damage(self):
        base_damage = self.get_base_damage() 
        damage_per_level = 10

        return base_damage + (self.level * damage_per_level) + self.equipped_item.damage
    

    def get_player_defence(self):
        base_defence = self.get_base_defence() 
        equipament_defence = 0
        defence_per_level = 10
        
        for piece_of_armor in self.equipped_armor:
            equipament_defence += piece_of_armor.defence

        return base_defence + (self.level * defence_per_level) + equipament_defence
    


    # Items

    def equip_piece_of_armor(self,wearable_item:WearableItem):
        equipped = False

        for piece_of_armor in self._equiped_armor:
            if piece_of_armor.wearable_type == wearable_item.wearable_type:
                index = self._equiped_armor.index(piece_of_armor)
                self._equiped_armor[index] = wearable_item
                equipped = True
                break
        
        if not equipped:
            self._equiped_armor.append(wearable_item) 


    def equip_item(self,item:Item):
        if item.is_equippable():
            if item.type == ITEM_TYPE_DAMAGE:
                self.equipped_item(item)
            else:
                self.equip_piece_of_armor(item)
        else:
            print("Esse item não pode ser equipado")


    def use_consumable(self,item:ConsumableItem):
        if item.effect_type == CONSUMABLE_EFFECT_TYPE_MANA:
            pass

    
    def serialize(self, title):
        # Serialize the player object to a dictionary
        player_info = {
            'player_id': self._player_id,
            'mana': self._mana,
            'game_class': self._game_class,
            'abilities': self._abilities, 
            'level': self._level,
            'xp': self._xp,
            'wallet': self._wallet.__dict__, 
            'inventory': self._inventory.__dict__,  
            'equipped_item': self._equipped_item.__dict__,  
            'equipped_armor': [item.__dict__ for item in self._equiped_armor],  
            'journal': self._journal.__dict__,  
            'name': self.name,
            'health': self.health,
            'race': self.race
        }

        return player_info


