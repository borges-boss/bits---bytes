from python.base.entity import Entity
from python.base.wallet import Wallet
from python.classes.inventory import Inventory
from python.base.ability import Ability
from python.classes.monster import Monster
from python.constants.constants import ABILITY_TYPE_PHYSICAL
from python.constants.constants import ABILITY_TYPE_MAGIC
from python.constants.constants import ABILITY_TYPE_STATS_HEALTH
from python.constants.constants import ABILITY_TYPE_STATS_STAMINA
from python.constants.constants import ABILITY_TYPE_STATS_DAMAGE
from python.constants.constants import ABILITY_TYPE_STATS_DEFENCE
from python.constants.constants import ABILITY_TYPE_STATS_TARG_HEALTH
from python.constants.constants import ABILITY_TYPE_STATS_TARG_STAMINA
from python.constants.constants import ABILITY_TYPE_STATS_TARG_DAMAGE
from python.constants.constants import ABILITY_TYPE_STATS_TARG_DEFENCE

class Player(Entity):

    def __init__(self, health, defence, race, type, player_id, name, mana, game_class, abilities, level, wallet:Wallet, inventory:Inventory):
        super().__init__(name, health, defence, race, type)
        self._player_id = player_id
        self._mana = mana
        self._game_class = game_class
        self._abilities = abilities
        self._level = level
        self._wallet = wallet
        self._inventory = inventory



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

    def deal_damage(self,ability:Ability, target:Monster):
        # Calcular dano baseado no nivel do player e o dano base da abilidade
        damage = self.level * ability.value

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

    def calculate_max_health(self):
        base_health = 100 
        health_per_level = 10

        return base_health + (self.level * health_per_level)

