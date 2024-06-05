from base.entity import Entity
from constants.constants import ABILITY_TYPE_MAGIC, ABILITY_TYPE_PHYSICAL
from constants.constants import ABILITY_TYPE_PHYSICAL, ABILITY_TYPE_STATS_ALL, ABILITY_TYPE_STATS_DAMAGE, ABILITY_TYPE_STATS_DEFENCE, ABILITY_TYPE_STATS_HEALTH, ABILITY_TYPE_STATS_MANA, ABILITY_TYPE_STATS_STAMINA, ABILITY_TYPE_STATS_TARG_DAMAGE, ABILITY_TYPE_STATS_TARG_DEFENCE, ABILITY_TYPE_STATS_TARG_HEALTH, ABILITY_TYPE_STATS_TARG_STAMINA, CLASS_TYPE_WARRIOR, CONSUMABLE_EFFECT_TYPE_DAMAGE, CONSUMABLE_EFFECT_TYPE_HEALTH, CONSUMABLE_EFFECT_TYPE_MANA, CONSUMABLE_EFFECT_TYPE_STAMINA, ITEM_TYPE_DAMAGE


class Monster(Entity):

    def __init__(self, health, damage, defence, stamina, race, type, name, mana, description, abilities, level):
        super().__init__(name,health, damage, defence, stamina, race, type)
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

    def use_stats_ability(self, ability, target):
        if self.mana >= ability.ability_cost:
            if ability.type == ABILITY_TYPE_STATS_HEALTH:
                self.health += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_STAMINA:
                self.stamina += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_MANA:
                self.mana += ability.effect_value
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
            elif ability.type == ABILITY_TYPE_STATS_ALL:
                self.defence += ability.effect_value
                self.damage += ability.effect_value
                self.health+= ability.effect_value
                self.stamina+= ability.effect_value
                self.mana+= ability.effect_value
            else:
                print("Tipo de abilidade invalido")
            if ability.type == ABILITY_TYPE_STATS_MANA:
                self.health-= ability.ability_cost
            else:
                self.mana-= ability.ability_cost
        else:
            print(f"{self.name} nao tem mana o suficiente para usar a abilidade {ability.name}")

    def dealDamage(self,ability, target):
        # Calcular dano baseado no nivel do monstro e o dano base da abilidade
        damage = self.level * (ability.value + self.damage)

         # Calcular redução de dano baseado na defesa do alvo
        damage_reduction = target.defence / 100.0 

        # Aplicar redução de dano
        net_damage = damage * (1 - damage_reduction)

        # Subtrair dano liquido da vida do alvo
        target.health -= net_damage
        print(f"\n{self.name} usou {ability.name}! {target.name} levou {net_damage} de dano.")

    def useAbility(self, ability, target):
        
        if ability.type == ABILITY_TYPE_PHYSICAL:
            self.dealDamage(ability,target)
            self.stamina-= ability.ability_cost
        elif ability.type == ABILITY_TYPE_MAGIC:
            self.dealDamage(ability,target)
            self.mana-= ability.ability_cost   
        else:
            self.use_stats_ability(ability,target) 
            
        return target
    


    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'damage': self.damage,
            'defence': self._defence,
            'stamina': self._stamina,
            'race': self._race,
            'type': self._type,
            'mana': self._mana,
            'description': self._description,
            'abilities': [ability.to_dict() for ability in self._abilities],
            'level': self._level
        }