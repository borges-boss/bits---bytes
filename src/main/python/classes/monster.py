from python.base.entity import Entity
from python.base.ability import Ability
from python.classes.player import Player
from python.constants.constants import ABILITY_TYPE_PHYSICAL

class Monster(Entity):

    def __init__(self, health, defence,stamina, race, type, name, mana, description, abilities, level):
        super().__init__(name,health, defence, stamina, race, type)
        self._mana = mana
        self._description = description
        self._abilities = abilities
        self._level = level


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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, value):
        self._abilities = value

    def dealDamage(self,ability:Ability, target:Player):
        # Calcular dano baseado no nivel do player e o dano base da abilidade
        damage = self.level * ability.value

         # Calcular redução de dano baseado na defesa do alvo
        damage_reduction = target.defence / 100.0 

        # Aplicar redução de dano
        net_damage = damage * (1 - damage_reduction)

        # Subtrair dano liquido da vida do alvo
        target.health -= net_damage
        print(f"{self.name} usou {ability.name}! {target.name} levou {net_damage} de dano!")

    def useAbility(self, ability:Ability, target:Player):
        
        if ability.type == ABILITY_TYPE_PHYSICAL:
            self.dealDamage(ability,target)
            self.stamina-= ability.ability_cost
        else:
            self.dealDamage(ability,target)
            self.mana-= ability.ability_cost    
            
        return target
