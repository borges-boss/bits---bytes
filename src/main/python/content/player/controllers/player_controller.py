from content.game_save.models.game_save_model import GameSaveModel
from content.player.models.player_model import PlayerModel
from base.ability import Ability
from base.item import Item
from base.journal import Journal
from base.wallet import Wallet
from classes.damage_item import DamageItem
from classes.inventory import Inventory
from classes.player import Player
from constants.constants import ABILITY_TYPE_MAGIC, ABILITY_TYPE_PHYSICAL, ABILITY_TYPE_STATS_ALL, ABILITY_TYPE_STATS_DAMAGE, ABILITY_TYPE_STATS_DEFENCE, ABILITY_TYPE_STATS_HEALTH, ABILITY_TYPE_STATS_MANA, ABILITY_TYPE_STATS_STAMINA, ABILITY_TYPE_STATS_TARG_DAMAGE, CLASS_TYPE_ASSASIN, CLASS_TYPE_BATTLE_MAGE, CLASS_TYPE_BERSERKER, CLASS_TYPE_MAGE, CLASS_TYPE_WARRIOR, ITEM_RARITY_COMMON, ITEM_TYPE_DAMAGE, RACE_TYPE_DWARF, RACE_TYPE_HALF_ELF, RACE_TYPE_HIGH_ELF, RACE_TYPE_HUMAN, RACE_TYPE_LIZARDFOLK, RACE_TYPE_ORC, STRUCTURE_TYPE_CAVE
from classes.cave import Cave


class PlayerController:

    global_player = None


    @classmethod
    def display_player_hud(cls, player):
        health_bar = '\033[31m' + '█' * int(player.health / 10) + '\033[0m'
        mana_bar = '\033[34m' + '█' * int(player.mana / 10) + '\033[0m'
        stamina_bar = '\033[32m' + '█' * int(player.stamina / 10) + '\033[0m'

        print(f"\033[31mHealth: {player.health}\033[0m [{health_bar:<10}]")
        print("")
        print(f"\033[34mMana: {player.mana}\033[0m [{mana_bar:<10}]")
        print("")
        print(f"\033[32mStamina: {player.stamina}\033[0m [{stamina_bar:<10}]")

    @classmethod
    def load_player(cls):
        model = GameSaveModel()
        cls.global_player = model.get_player_info()

    @classmethod
    def save_player_state(cls,player):
        model = GameSaveModel()
        model.save_game(player)
        print("O seu jogo foi salvo!")

    @classmethod
    def save_player(cls,player):
        model = GameSaveModel()
        model.save_game(player)

    @classmethod
    def get_player(cls):
        cls.load_player()
        if cls.get_player == None:
            cls.load_player()

        return cls.global_player
    
    @classmethod
    def set_player_state(cls, player):
        cls.global_player = player

    @classmethod
    def restore_full_health(cls,player):
        player_model = PlayerModel()
        player.health = player_model.get_player_max_health(cls.global_player) #Restaurar vida completa do jogador
        return player

    @classmethod
    def restore_full_mana(cls,player):
        player_model = PlayerModel()
        player.mana = player_model.get_player_max_mana(cls.global_player)
        return player

    @classmethod
    def restore_full_stamina(cls,player):
        player_model = PlayerModel()
        player.stamina = player_model.get_player_max_stamina(cls.global_player)
        return player

    @classmethod
    def equip_piece_of_armor(cls,wearable_item):
        player_model = PlayerModel()
        cls.set_player_state(player_model.equip_piece_of_armor(wearable_item, cls.get_player()))

    @classmethod
    def equip_item(cls,item):
        player_model = PlayerModel()
        cls.set_player_state(player_model.equip_item(item,cls.get_player()))

    @classmethod
    def use_consumable(cls,item):
        player_model = PlayerModel()
        cls.set_player_state(player_model.use_consumable(item,cls.get_player()))

    @classmethod
    def useAbility(cls, ability, target, player):
        player_model = PlayerModel()
        return player_model.useAbility(ability,target,player)
    
    @classmethod
    def get_player_damage(cls):
        player_model = PlayerModel()
        return player_model.get_player_damage(cls.get_player())
    
    @classmethod
    def get_player_defence(cls):
        player_model = PlayerModel()
        return player_model.get_player_defence(cls.get_player())
    

    @classmethod
    def reset_player_status(cls):
        player_mode = PlayerModel()
        cls.get_player().damage = player_mode.get_player_damage(cls.get_player())
        cls.get_player().defence = player_mode.get_player_defence(cls.get_player())


    @classmethod
    def init_new_player_instance(cls):
        initial_item = DamageItem("Punhos",ITEM_TYPE_DAMAGE,ITEM_RARITY_COMMON,0,[],1.0)
        cls.global_player = Player(0,0,0,0,"","","",[],1,0,Wallet(0),Inventory([],500.0),initial_item,[],Journal([]),Cave("",STRUCTURE_TYPE_CAVE,1,[],[]),"")
        cls.global_player.inventory.add_item(initial_item)
        model = GameSaveModel()
        model.save_game(cls.global_player)

    @classmethod
    def init_player_attributes(cls):
        player_mode = PlayerModel()
        player = cls.get_player()
        player.health = player_mode.get_player_max_health(player)
        player.mana = player_mode.get_player_max_mana(player)
        player.stamina = player_mode.get_player_max_stamina(player)
        player.damage = player_mode.get_player_damage(player)
        player.defence = player_mode.get_player_defence(player)
        model = GameSaveModel()
        model.save_game(player)
        return player


    @classmethod
    def init_player_abilities(cls):
        player = cls.get_player()

        if player.game_class == CLASS_TYPE_WARRIOR:
            player.abilities.append(Ability("Golpe Poderoso", "Um ataque corpo a corpo poderoso.", ABILITY_TYPE_PHYSICAL, 50, 10))
            player.abilities.append(Ability("Defender", "Aumenta a defesa durante a batalha", ABILITY_TYPE_STATS_DEFENCE, 20, 5))

        elif player.game_class == CLASS_TYPE_MAGE:
            player.abilities.append(Ability("Bola de Fogo", "Um ataque à distância flamejante.", ABILITY_TYPE_MAGIC, 40, 15))
            player.abilities.append(Ability("Curar", "Restaura um pouco de saúde.", ABILITY_TYPE_STATS_HEALTH, 30, 20))

        elif player.game_class == CLASS_TYPE_ASSASIN:
            player.abilities.append(Ability("Ataque Surpresa", "Um ataque rápido e surpreendente.", ABILITY_TYPE_PHYSICAL, 60, 10))
            player.abilities.append(Ability("Esconder", "Fica invisível e aumenta sua defesa", ABILITY_TYPE_STATS_DEFENCE, 30, 5))

        elif player.game_class == CLASS_TYPE_BERSERKER:
            player.abilities.append(Ability("Fúria", "Aumenta o dano causado durante a batalha", ABILITY_TYPE_STATS_DAMAGE, 70, 10))
            player.abilities.append(Ability("Resistir", "Ignora parte do dano recebido.", ABILITY_TYPE_STATS_DEFENCE, 30, 5))

        elif player.game_class == CLASS_TYPE_BATTLE_MAGE:
            player.abilities.append(Ability("Raio Arcano", "Um ataque mágico à distância.", ABILITY_TYPE_MAGIC, 50, 15))
            player.abilities.append(Ability("Escudo Mágico", "Cria um escudo que absorve parte do dano recebido.", ABILITY_TYPE_STATS_DEFENCE, 25, 10))

        if player.race == RACE_TYPE_HUMAN:
            player.abilities.append(Ability("Determinação", "Aumenta todas as estatísticas durante a batalha", ABILITY_TYPE_STATS_ALL, 10, 10))

        elif player.race == RACE_TYPE_DWARF:
            player.abilities.append(Ability("Pele de Pedra", "Aumenta a defesa durante a batalha", ABILITY_TYPE_STATS_DEFENCE, 20, 5))

        elif player.race == RACE_TYPE_HALF_ELF:
            player.abilities.append(Ability("Encanto", "Confunde o inimigo, reduzindo seu dano.", ABILITY_TYPE_STATS_TARG_DAMAGE, 15, 10))

        elif player.race == RACE_TYPE_LIZARDFOLK:
            player.abilities.append(Ability("Regeneração", "Recupera um pouco de saúde.", ABILITY_TYPE_STATS_HEALTH, 10, 5))

        elif player.race == RACE_TYPE_ORC:
            player.abilities.append(Ability("Força Bruta", "Aumenta o dano causado durante a batalha", ABILITY_TYPE_STATS_DAMAGE, 25, 10))

        elif player.race == RACE_TYPE_HIGH_ELF:
            player.abilities.append(Ability("Sabedoria Antiga", "Sacrifica um pouco de vida para aumentar a mana durante a batalha", ABILITY_TYPE_STATS_MANA, 30, 10))

        #Ataque basico para todas as classes e raças
        player.abilities.append(Ability("Bater", "Um ataque basico que usa oque voce tiver na mao para atacar o inimigo (O dano da abilidade aumenta dependendo do que voce tem equipado)", ABILITY_TYPE_PHYSICAL, 1, 4))

        model = GameSaveModel()
        model.save_game(player)
        cls.global_player = player
        
    @classmethod
    def add_exp(cls, xp_amount):
        player = cls.get_player()
        player.xp += xp_amount

        # Define a quantidade de XP necessária para subir de nível
        xp_to_level_up = 100 * player.level

        # Verifica se o jogador tem XP suficiente para subir de nível
        while player.xp >= xp_to_level_up:
            # Aumenta o nível do jogador e redefine seu XP
            player.level += 1
            player.xp -= xp_to_level_up

            # Aumenta a quantidade de XP necessária para o próximo nível
            xp_to_level_up = 100 * player.level
            print(f"\nVoce subiu de nivel {player.level}!")
            cls.init_player_attributes() #Re-caulcular player stats
            





        
    
