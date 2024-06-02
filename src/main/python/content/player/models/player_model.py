from constants.constants import ABILITY_TYPE_MAGIC, ABILITY_TYPE_PHYSICAL, ABILITY_TYPE_STATS_DAMAGE, ABILITY_TYPE_STATS_DEFENCE, ABILITY_TYPE_STATS_HEALTH, ABILITY_TYPE_STATS_STAMINA, ABILITY_TYPE_STATS_TARG_DAMAGE, ABILITY_TYPE_STATS_TARG_DEFENCE, ABILITY_TYPE_STATS_TARG_HEALTH, ABILITY_TYPE_STATS_TARG_STAMINA, CLASS_TYPE_WARRIOR, CONSUMABLE_EFFECT_TYPE_HEALTH, CONSUMABLE_EFFECT_TYPE_MANA, ITEM_TYPE_DAMAGE
from constants.constants import CLASS_TYPE_ASSASIN
from constants.constants import CLASS_TYPE_MAGE
from constants.constants import CLASS_TYPE_BATTLE_MAGE
from constants.constants import CLASS_TYPE_BERSERKER
from constants.constants import RACE_TYPE_HUMAN
from constants.constants import RACE_TYPE_DWARF
from constants.constants import RACE_TYPE_HALF_ELF
from constants.constants import RACE_TYPE_LIZARDFOLK
from constants.constants import RACE_TYPE_ORC


class PlayerModel:

    def get_base_health(self, player):
        base_health = 100

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_health += 50
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_health += 20
        elif player.game_class == CLASS_TYPE_MAGE:
            base_health += 10
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_health += 30
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_health += 60

        if player.race == RACE_TYPE_HUMAN:
            base_health += 10
        elif player.race == RACE_TYPE_DWARF:
            base_health += 20
        elif player.race == RACE_TYPE_HALF_ELF:
            base_health += 15
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_health += 20
        elif player.race == RACE_TYPE_ORC:
            base_health += 25

        return base_health
        
    def get_base_mana(self, player):
        base_mana = 100

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_mana += 20
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_mana += 30
        elif player.game_class == CLASS_TYPE_MAGE:
            base_mana += 60
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_mana += 50
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_mana += 40

        if player.race == RACE_TYPE_HUMAN:
            base_mana += 10
        elif player.race == RACE_TYPE_DWARF:
            base_mana += 20
        elif player.race == RACE_TYPE_HALF_ELF:
            base_mana += 15
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_mana += 20
        elif player.race == RACE_TYPE_ORC:
            base_mana += 25

        return base_mana

    def get_base_stamina(self, player):
        base_stamina = 100

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_stamina += 60
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_stamina += 50
        elif player.game_class == CLASS_TYPE_MAGE:
            base_stamina += 20
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_stamina += 40
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_stamina += 70

        if player.race == RACE_TYPE_HUMAN:
            base_stamina += 10
        elif player.race == RACE_TYPE_DWARF:
            base_stamina += 20
        elif player.race == RACE_TYPE_HALF_ELF:
            base_stamina += 15
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_stamina += 20
        elif player.race == RACE_TYPE_ORC:
            base_stamina += 25

        return base_stamina
        
    def get_base_damage(self, player):
        base_damage = 10

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_damage += 20
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_damage += 30
        elif player.game_class == CLASS_TYPE_MAGE:
            base_damage += 10
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_damage += 15
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_damage += 25

        if player.race == RACE_TYPE_HUMAN:
            base_damage += 5
        elif player.race == RACE_TYPE_DWARF:
            base_damage += 10
        elif player.race == RACE_TYPE_HALF_ELF:
            base_damage += 7
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_damage += 10
        elif player.race == RACE_TYPE_ORC:
            base_damage += 12

        return base_damage

    def get_base_defence(self, player):
        base_defence = 10

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_defence += 30
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_defence += 20
        elif player.game_class == CLASS_TYPE_MAGE:
            base_defence += 10
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_defence += 20
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_defence += 40

        if player.race == RACE_TYPE_HUMAN:
            base_defence += 5
        elif player.race == RACE_TYPE_DWARF:
            base_defence += 10
        elif player.race == RACE_TYPE_HALF_ELF:
            base_defence += 7
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_defence += 10
        elif player.race == RACE_TYPE_ORC:
            base_defence += 12

        return base_defence

 
    def get_player_max_health(self, player):
        base_health = player.get_base_health() 
        health_per_level = 10

        return base_health + (player.level * health_per_level)
    

    def get_player_max_mana(self, player):
        base_mana = player.get_base_mana() 
        mana_per_level = 10

        return base_mana + (player.level * mana_per_level)
    

    def get_player_max_stamina(self, player):
        base_stamina = player.get_base_stamina() 
        stamina_per_level = 10

        return base_stamina + (player.level * stamina_per_level)
    

    def equip_piece_of_armor(self,wearable_item, player):
        equipped = False

        for piece_of_armor in self.equiped_armor:
            if piece_of_armor.wearable_type == wearable_item.wearable_type:
                index = player.equiped_armor.index(piece_of_armor)
                player.equiped_armor[index] = wearable_item
                equipped = True
                break
        
        if not equipped:
            player.equiped_armor.append(wearable_item) 

        return player

    def equip_item(self,item,player):
        if item.is_equippable():
            if item.type == ITEM_TYPE_DAMAGE:
                player.equipped_item(item)
            else:
                self.equip_piece_of_armor(item,player)
        else:
            print("Esse item não pode ser equipado")


    def use_consumable(self,item, player):
        if item.effect_type == CONSUMABLE_EFFECT_TYPE_MANA:
            new_mana = (player.mana + item.effect_value)

            if new_mana <= self.get_player_max_mana(player):
             player.mana(player.mana + item.effect_value)
            else:
                player.mana(self.get_player_max_mana(player))

        elif  item.effect_type == CONSUMABLE_EFFECT_TYPE_HEALTH:
            new_health = (player.health + item.effect_value)

            if new_health <= self.get_player_max_health(player):
                    player.health(new_health)
            else:
                 player.health(self.get_player_max_health(player))

        else:
            new_stamina = (player.stamina + item.effect_value)
            
            if new_stamina <= self.get_player_max_stamina(player):
                    player.stamina(new_stamina)
            else:
                 player.stamina(self.get_player_max_stamina(player))

        return player
    

    def deal_damage(self, ability, target):
        # Calcular dano baseado no nivel do player e o dano base da abilidade
        damage = ability.value + self.damage

         # Calcular redução de dano baseado na defesa do alvo
        damage_reduction = target.defence / 100.0 

        # Aplicar redução de dano
        net_damage = damage * (1 - damage_reduction)

        # Subtrair dano liquido da vida do alvo
        target.health(target.health - net_damage)
        print(f"{self.name} usou {ability.name}! {target.name} levou {net_damage} de dano!")
        return target


    def use_stats_ability(self, ability, target, player):
        if player.mana >= ability.ability_cost:
            if ability.type == ABILITY_TYPE_STATS_HEALTH:
                player.health += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_STAMINA:
                player.stamina += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_DAMAGE:
                player.damage += ability.effect_value
            elif ability.type == ABILITY_TYPE_STATS_DEFENCE:
                player.defence += ability.effect_value
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
            
            player.mana(player.mana - ability.ability_cost)
        else:
            print("Not enough mana to use this ability.")

        return player


    def useAbility(self, ability, target, player):
        if ability.type == ABILITY_TYPE_PHYSICAL:
            if player.stamina >= ability.ability_cost:
                target = self.deal_damage(ability,target)
                player.stamina(player.stamina - ability.ability_cost)
            else:
                print("Voce não tem stamina o suficiente para usar essa abilidade")
        elif ability.type == ABILITY_TYPE_MAGIC:
            if player.mana >= ability.ability_cost:
                self.deal_damage(ability,target)
                player.mana(player.mana - ability.ability_cost)
            else:
                print("Voce não tem mana o suficiente para usar essa abilidade")
        else:
            self.use_stats_ability(ability,target,player)

        return target
    


    def get_base_damage(self, player):
        base_damage = 10

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_damage += 20
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_damage += 30
        elif player.game_class == CLASS_TYPE_MAGE:
            base_damage += 10
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_damage += 15
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_damage += 25

        if player.race == RACE_TYPE_HUMAN:
            base_damage += 5
        elif player.race == RACE_TYPE_DWARF:
            base_damage += 10
        elif player.race == RACE_TYPE_HALF_ELF:
            base_damage += 7
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_damage += 10
        elif player.race == RACE_TYPE_ORC:
            base_damage += 12

        return base_damage

    def get_base_defence(self, player):
        base_defence = 10

        if player.game_class == CLASS_TYPE_WARRIOR:
            base_defence += 30
        elif player.game_class == CLASS_TYPE_ASSASIN:
            base_defence += 20
        elif player.game_class == CLASS_TYPE_MAGE:
            base_defence += 10
        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            base_defence += 20
        elif player.game_class == CLASS_TYPE_BERSERKER:
            base_defence += 40

        if player.race == RACE_TYPE_HUMAN:
            base_defence += 5
        elif player.race == RACE_TYPE_DWARF:
            base_defence += 10
        elif player.race == RACE_TYPE_HALF_ELF:
            base_defence += 7
        elif player.race == RACE_TYPE_LIZARDFOLK:
            base_defence += 10
        elif player.race == RACE_TYPE_ORC:
            base_defence += 12

        return base_defence

    def get_player_damage(self, player):
        base_damage = self.get_base_damage(player) 
        damage_per_level = 10
        extra_dmg_from_item = (player.equipped_item.damage if player.equipped_item != None else 0)
        return base_damage + (player.level * damage_per_level) + extra_dmg_from_item
    
    
    def get_player_defence(self,player):
        base_defence = self.get_base_defence(player) 
        equipament_defence = 0
        defence_per_level = 10
        
        for piece_of_armor in player.equipped_armor:
            equipament_defence += piece_of_armor.defence

        return base_defence + (player.level * defence_per_level) + equipament_defence